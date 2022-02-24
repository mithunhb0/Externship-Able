from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email = self.normalize_email(email),            
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            email = self.normalize_email(email),            
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    phone_number    = models.CharField(max_length=10)
    email           = models.EmailField(max_length=100, unique=True)
    

    # required
    STATUS_CHOICES = (('sales representative', 'Sales representative'),('sales admin', 'Sales admin'))
    user_type       = models.CharField(max_length=50, choices=STATUS_CHOICES, default='sales representative')
    created_at      = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now=True)
    is_staff        = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)
    is_approved     = models.BooleanField(default=False)
    manager_id      = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superadmin

    def has_module_perms(self, add_label):
        return True