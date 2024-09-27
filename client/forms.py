from django import forms
from .models import UserModel

class RegisterForm(forms.ModelForm):
    class Meta:
       model = UserModel
       fields = ['user_name','phone_number','email_address','password','latitude','longitude']
       widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control border border-black', 'placeholder': 'Username'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control border border-black', 'placeholder': 'Phone Number'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control border border-black', 'placeholder': 'Email Address'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control  border border-black', 'placeholder': 'Password'}),
            'latitude':forms.HiddenInput(),
            'longitude':forms.HiddenInput()
        }
   