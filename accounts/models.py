from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager

from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    pass


class User(AbstractUser):
    pass
