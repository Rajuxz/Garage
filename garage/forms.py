from django import forms
class LoginForm(forms.Form):
    email = forms.EmailInput(required = True,attrs={'placeholder':'Email Address'})
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    def clean(self):
        cleaned_data = super().clean() #parent's clean method.
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        return cleaned_data