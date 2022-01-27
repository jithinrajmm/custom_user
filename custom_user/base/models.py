from distutils.archive_util import make_zipfile
import email
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200,unique=True)
    bio = models.TextField(max_length=100,null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # the major difference bet ween the AbstractUser and AbstractBaseUser is 
    #  the feilds we can add and use the existing fields in user in AbstractUser

    # the feilds must be build from scratch in the AbstractBaseUser


# Create your models here.
