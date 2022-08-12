from django.db import models
from django.contrib.auth.models import AbstractUser as BaseAbstractUser, UserManager as BaseUserManager
from django.utils import timezone



class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('user must have email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
                email=email,
                is_staff=is_staff,
                is_active=True,
                is_superuser=is_superuser,
                last_login=now,
                date_joined=now,
                **extra_fields
                )
        # We check if password has been given
        if password:
            user.set_password(password)
            user.save(using=self._db)
            return user

    #We change following functions signature to allow "No password"
    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        user=self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(BaseAbstractUser):
    updated_at = models.DateTimeField(auto_now=True)
    username   = None
    email    = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()