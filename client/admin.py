from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel

class CustomUserAdmin(UserAdmin):
    model = UserModel
    list_display = ('user_name','email_address','created_at','is_staff','is_superuser')
    list_filter = ('is_active','is_staff')
    # fieldsets = (
    #     (None, {
    #         "fields": (
    #              'email_address','password'
    #         ),
            
    #     }),
    #     ('Personal Information',{"fields":('user_name'),})
    # )
    search_fields = ('email_address','user_name',)
    ordering = ('email_address',)
    
    
    
    

admin.site.register(UserModel,CustomUserAdmin)



    