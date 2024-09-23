from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import UserManager
import uuid

class UserModel(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user_name = models.CharField(verbose_name='User Name',blank=False,max_length=50)
    email_address = models.EmailField(verbose_name='Email Address',blank=False,unique=True)
    phone_number = models.CharField(verbose_name="Phone Number",blank=True,max_length=15)
    latitude = models.FloatField(verbose_name='Latitude',default=0.0)
    longitude = models.FloatField(verbose_name='Longitude',default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()
    '''
        Standerd term is object. It is used when using create_user method as User.objects.create_user()
    '''
    USERNAME_FIELD = 'email_address'
    REQUIRED_FIELDS = ['user_name'] #prompted while creating a user via createsuperuser command.
    
    def __str__(self):
        return self.user_name
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
