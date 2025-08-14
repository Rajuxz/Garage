from .models import Request

from datetime import timedelta
from django.utils import timezone
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from datetime import timedelta
import pandas as pd

def predict_requests():
    # Getting past data
    recent_requests = Request.objects.filter(date__gte=timezone.now() - timedelta(days=365))

    print(f'Requests: {recent_requests.count()}')  # Print the number of requests found

    # Converting it to pandas DataFrame
    data = pd.DataFrame(list(recent_requests.values('date', 'category', 'cost')))

    print("Raw data from the database:")
    print(data)  # Print the raw data

    if data.empty:
        print('Empty dataset.')
        return []  # Return an empty list if no data is available

    # Correctly convert the 'date' column to datetime and handle errors
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    print(f"Converted dates: {data['date']}")  # Print the converted date column

    # Check if the conversion resulted in any NaT (not a time) values
    if data['date'].isnull().any():
        print("There are NaT values in the date column.")
        return []  # Return empty if there's an issue

    # Extract additional time-related features
    data['day_of_week'] = data['date'].dt.dayofweek
    data['day'] = data['date'].dt.day
   
    # Aggregate the data by date to get the number of requests per day
    daily_data = data.groupby('date').agg({
    'day_of_week': 'first',  # Use 'first' because it's the same for all rows on the same date
    'day': 'first',
    'category': 'count'  # Assuming 'category' represents requests
}).reset_index().rename(columns={'category': 'requests_per_day'})

    print("Daily data after aggregation:")
    print(daily_data)  # Print the aggregated daily data

    # Check the number of samples
    if len(daily_data) < 2:  # Less than 2 samples
        print("Not enough samples to perform train-test split. Using available data directly for predictions.")
        # Use the single data point for prediction directly (for demonstration)
        single_sample = daily_data.iloc[0]
        future_dates = pd.DataFrame({
            'date': pd.date_range(start=timezone.now().date() + timedelta(days=1), periods=7)
        })
        future_dates['predicted_requests'] = single_sample['requests_per_day']  # Use the same value for all future dates
        return list(zip(future_dates['date'], future_dates['predicted_requests']))

    # Extract features and target variable
    X = daily_data[['day_of_week', 'day']]  # Features
    y = daily_data['requests_per_day']       # Target variable

    # Train-test split (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Creating DataFrame with data for the next 7 days
    future_dates = pd.DataFrame({
        'date': pd.date_range(start=timezone.now().date() + timedelta(days=1), periods=7)  # Start from tomorrow
    })

    # Extract day and day_of_week for these future dates
    future_dates['day_of_week'] = future_dates['date'].dt.dayofweek
    future_dates['day'] = future_dates['date'].dt.day

    # Use the model to predict the number of requests for the next 7 days
    future_predictions = model.predict(future_dates[['day_of_week', 'day']])

    # Add the predictions to the future_dates DataFrame
    future_dates['predicted_requests'] = future_predictions

    print(f"Future dates with predictions:\n{future_dates}")

    return list(zip(future_dates['date'], future_predictions))
