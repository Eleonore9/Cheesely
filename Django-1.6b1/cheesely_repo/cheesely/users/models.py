# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser
# Import the basic Django ORM models library
from django.db import models

# Subclass AbstractUser
class User(AbstractUser):
	tagline = models.CharField("TagLine", 
			max_length=176, blank=True)


