from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse

# Create your models here.
USERNAME_REGEX = '^[a-zA-Z0-9]*$'
NAME_REGEX = '^[a-zA-Z]*$'


class User(AbstractUser):
        username = models.CharField(max_length=256, unique=True, blank=False,
                                validators=[
                                        RegexValidator(
                                        regex = USERNAME_REGEX,
                                        message = 'Username must be Alpahnumeric',
                                        code='invalid_username'
                                        )]
                                )
        first_name = models.CharField(max_length=256, blank=False,
                                  validators=[
                                        RegexValidator(
                                        regex = NAME_REGEX,
                                        message = 'Name must be Alphabetic',
                                        code='invalid_first_name'
                                        )]
                                )
        last_name = models.CharField(max_length=256, blank=False,
                                  validators=[
                                        RegexValidator(
                                        regex = NAME_REGEX,
                                        message = 'Name must be Alphabetic',
                                        code='invalid_last_name'
                                        )]
                                )
        email = models.EmailField(unique=True, blank=False)
        bio = models.CharField(max_length=512, blank=True)
        birth_date = models.DateField(null=True, blank=False)

        USERNAME_FIELD = 'email' 
        REQUIRED_FIELDS = ['username'] 

        def __str__(self):
                return self.username
        
        def get_absolute_url(self):
                return reverse("user_profile", kwargs={"username": self.username})
                