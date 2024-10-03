from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

UserModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None
        try:
            user = UserModel.objects.get(email_address=username)
            if user.check_password(password):
                print(user)
                return user
            else:
                print("Authentication.py : Else is running.")
                return None
        except UserModel.DoesNotExist:
            print("Authentication.py : No user exists with given email.")
            return None
        
