from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'})
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password','class':'form-control'}
        ))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        print(f'cleaned data: {cleaned_data}')
        print(username,password)
        if username and password:
            user = authenticate(username = username, password = password)
            print(f'forms.py: {user}')
            if user is None:
                #This portion will check and raise errors following errors:
                # If  user exists but authentication fails, that means password is incorrect.
                # If no, email is not registered.
                from django.contrib.auth import get_user_model
                UserModel = get_user_model()
                if UserModel.objects.filter(email_address = username).exists():
                    print("Forms.py: Password mismatch.")
                    self.add_error('password',f'Password does not matched')
                else:
                    print("Forms.py: Invalid email.")
                    self.add_error('username','Invalid email address.')
        return cleaned_data
    

    def confirm_login_allowed(self, user):
        # This method can be used to raise errors for specific conditions.
        if not user.is_active:
            raise ValidationError('This account is inactive.')