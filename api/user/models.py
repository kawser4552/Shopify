from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,PermissionsMixin,BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError("User must have email")
        
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password):
        user=self.create_user(email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=50, default='Anonymous')
    email = models.EmailField(max_length=254,unique = True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects=CustomUserManager()
    

    # username = None


    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    
    

    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)

    session_token = models.CharField(max_length=10,default=0) 

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.email
    
    





# class CustomUser(AbstractUser):
#     name = models.CharField(max_length=50, default='Anonymous')
#     email = models.EmailField(max_length=254,unique = True)

#     username = None


#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     phone = models.CharField(max_length=20, blank=True, null=True)
#     gender = models.CharField(max_length=20, blank=True, null=True)

#     session_token = models.CharField(max_length=10,default=0)

#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)