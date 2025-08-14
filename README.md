# Garage management System

This project is a Django-based web application for managing vehicle repair and maintenance services. Customers can submit service requests for their vehicles, specifying repair or maintenance needs. The admin can review these requests, assign them to available mechanics, and monitor progress. Mechanics can log in, update the status of assigned jobs, and mark work as completed. The system helps track service requests from start to finish, making the process easier for both customers and service providers.

## Customer

- customer will signup and login into system
- customer can make request for service of their vehicle by providing details (vehicle number, model, problem description etc.)
- After Request approved by admin, customer can check cost, status of service
- customer can delete request (Enquiry) if customer change their mind or not approved by admin (ONLY PENDING REQUEST CAN BE DELETED )
- customer can check status of Request(Enquiry) that is Pending, Approved, Repairing, Repairing Done, Released
- customer can check invoice details or repaired vehicles
- customer can send feedback to admin
- customer can see/edit their profile

---

## Mechanic

- mechanic will apply for job by providing details like (skills, address, mobile etc.)
- Admin will hire(approve) mechanic account based on skill
- After account approval, mechanic can login into system
- mechanic can see how many work (vehicles to repair) is assigned to me
- mechanic can change status of service ('Repairing', 'Repairing Done') according to work progress
- mechanic can see salary and how many vehicles he/she have repaired so far
- mechanic can send feedback to admin
- mechanic can see/edit their profile

---

### Admin

- First admin will login ( for username/password run following command in cmd )

```
py manage.py createsuperuser
```

- Give username, email, password and your admin account will be created.
- After login , admin can see how many customer, mechanic, recent service orders on dashboard
- Admin can see/add/update/delete customers
- Admin can see each customer invoice (if two request made by same customer it will show total sum of both request)
- Admin can see/add/update/delete mechanics
- Admin can approve(hire) mechanics (requested by mechanic) based on their skills
- Admin can see/update mechanic salary
- Admin can see/update/delete request/enquiry for service sent by customer
- Admin can also make request for service (suppose customer directly reached to service center/office)
- Admin can approve request for service made by customer and assign to mechanic for repairing and will provide cost according to problem description
- Admin can see all service cost of request (both approved and pending)
- Admin can see feedbacks sent by customer/mechanic

---

### Other Features

- we can change theme of website day(white) and night(black)
- if customer is deleted by admin then their request(Enquiry) will be deleted automatically

#### Request Volume Prediction

The `predict_requests()` function forecasts the number of requests for the next 7 days based on historical request data from the past year.

### How It Works

1. **Data Retrieval**

   - Fetches `date`, `category`, and `cost` fields from the `Request` model for the last 365 days.

2. **Data Preparation**

   - Converts `date` to a valid datetime format.
   - Extracts `day_of_week` and `day` as features.
   - Aggregates requests per day.

3. **Edge Case Handling**

   - If no data or invalid dates exist, returns an empty list.
   - If fewer than 2 days of data are available, reuses the existing value for future predictions.

4. **Model Training**

   - Uses `LinearRegression` from scikit-learn.
   - Features: `day_of_week`, `day`.
   - Target: Requests per day.
   - Splits data into training (80%) and testing (20%) sets.

5. **Prediction**
   - Generates dates for the next 7 days.
   - Predicts daily request counts for each date.
   - Returns a list of `(date, predicted_requests)` tuples.

### Returns

```python
[
    (datetime.date, float),  # Example: (2025-08-15, 12.3)
    ...
]


```

# HOW TO RUN THIS PROJECT

- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :

```
pip install django==3.0.5
pip install django-widget-tweaks

```

- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :

```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```

- Now enter following URL in Your Browser Installed On Your Pc

```
http://127.0.0.1:8000/
```

## CHANGES REQUIRED FOR CONTACT US PAGE

- In settins.py file, You have to give your email and password

```
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'your email password'
EMAIL_RECEIVING_USER = 'youremail@gmail.com'
```

- Login to gmail through host email id in your browser and open following link and turn it ON

```
https://myaccount.google.com/lesssecureapps
```

## Team

- Rabin Adhikari (Frontend portion)
- Rajan Khanal (Core backend and database + documentation)
