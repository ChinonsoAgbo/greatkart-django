from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class myAccountManager(BaseUserManager):
    
################################ creating a normal user #################################
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        if not username:
            raise ValueError('Users must have an username')
        
        user = self.model(
            email = self.normalize_email(email), # make email lowercase 
            first_name=first_name, 
            last_name=last_name,
        )
        user.set_password(password) # set password
        user.save(using=self._db) # save user
        return user
    
################################ creating superuser #################################
    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user( # create user parameters for superuser
            email = self.normalize_email(email), # make email lowercase 
            first_name=first_name, 
            last_name=last_name,
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using = self._db) # save user
        return user

#Class represents custom user model 
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    #required 
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)


    USERNAME_FIELD =  'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name']

    objects = myAccountManager() 

    def __str__(self):
        return self.email #return the email on the template 
    
    ################################ for admin only #################################
    def has_perm(self, perm, obj=None):
        return self.is_admin 
    
    def has_module_perms(self, app_label):
        return True

# create account manager 