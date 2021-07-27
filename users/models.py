import datetime
import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


# custom User manager
class CustomManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, password):
        user = self.model(firstname=firstname, lastname=lastname,
                          email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, firstname, lastname, email, password):
        user = self.create_user(
            firstname=firstname, lastname=lastname, email=email, password=password)
        user.is_admin = True
        user.save()
        return user


# Custom User Model
class User(AbstractBaseUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    firstname = models.CharField(max_length=35)
    lastname = models.CharField(max_length=35)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    data = models.OneToOneField(
        'UserData', related_name='user', on_delete=models.CASCADE, null=True)
    REQUIRED_FIELDS = ['firstname', 'lastname', 'password']
    USERNAME_FIELD = 'email'
    objects = CustomManager()

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['firstname', ]

    def get_full_name(self):
        return '{0} {1}'.format(self.firstname, self.lastname)

    def __str__(self):
        return '{0} {1}'.format(self.firstname, self.lastname)

    def is_staff(self):
        return self.is_admin

    def has_perm(self, app=None):
        return True

    def has_module_perms(self, app_label=None):
        return True


# User data
class UserData(models.Model):
    country = models.CharField(max_length=48, default='null', null=True)
    state = models.CharField(max_length=48, default='null', null=True)
    phone = models.CharField(max_length=15, default='null', null=True)
    picture = models.ImageField(null=True)
    dob = models.DateField(null=True)

    def __str__(self):
        return "data"


# Verification Code
class VerificationCode(models.Model):
    email = models.EmailField(max_length=255)
    generated_at = models.DateTimeField(default=timezone.now, editable=False)
    code = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.code

    def is_valid(self):
        elapsed = timezone.now() - self.generated_at
        print(elapsed)
        return True
