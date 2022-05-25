from enum import unique
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin


# Create your models here.

class Teachermanager(BaseUserManager):
    def create_user(self, email, name, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError("email is required")
        if not name:
            raise ValueError("name is required")
        now = timezone.now()
        email = self.normalize_email(email)
        teacher = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields


        )
        teacher.set_password(password)
        teacher.save(using=self._db)
        return teacher

    def create_superuser(self, email, name, password):
        teacher = self.create_user(email, name, password, True, True)
        return teacher


class Teacher(AbstractBaseUser):
    image = models.ImageField(width_field=40, height_field=40, upload_to='teacher-profile/', null=True, blank=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True, max_length=250)
    subject = models.CharField(max_length=250)
    password = models.CharField(max_length=250, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['name']

    objects = Teachermanager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
