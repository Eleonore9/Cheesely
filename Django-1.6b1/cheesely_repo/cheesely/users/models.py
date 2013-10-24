# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models library
from django.db import models

# Import/alias the ugettext_lazy internationalization function
from django.utils.translation import ugettext_lazy as _

# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models library
from django.db import models

class User(AbstractUser):
	    # Internationalized tagline model field label
	        tagline = models.CharField(_("Tag Line"),
				             max_length=176,
					     blank=True)
