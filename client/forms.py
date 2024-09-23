from django import forms
from .models import UserModel

class RegisterForm(forms.ModelForm):
    class Meta:
       model = UserModel
       fields = ['user_name','phone_number','email_address','password']
       widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control ', 'placeholder': 'Password'}),
        }
   
    #Overriding form field initialization.
    # def __init__(self,*args,**kwargs) -> None:
    #     super(RegisterForm,self).__init__(*args,**kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs.update({'class':'form-control form-floating'})