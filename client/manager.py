from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):
    def create_user(self,email_address,password = None, **extra_fields):
        if not email_address:
            raise ValueError("Email field is required !")
        if not password:
            raise ValueError("Password field is required !")
        
        email = self.normalize_email(email_address)
        """
        We pass phone number, name etc here. It create the user model with the provided email and any additional field preparing it for saving to the database.
        """
        user = self.model(email_address = email_address, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_address, password,**extra_fields):
        """
        Create and return superuser with an email and password
        """
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email_address,password,**extra_fields)