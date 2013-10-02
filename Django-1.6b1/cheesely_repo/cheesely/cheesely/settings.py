"""
Django settings for cheesely project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wef0tflpwg%*zt3=d@)d5y2c6jqhx^r=zuyctin#g%aw3pp_ga'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Handles database migrations
    'south',
    'cheeses',
    # Custom users app
    'users',
    # Handles user registration
    'registration',
    # Handles user registration themes
    'registration_bootstrap',
    # Improves django from layouts
    'crispy_forms',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cheesely.urls'

WSGI_APPLICATION = 'cheesely.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    },
    'postgresql': {
	    'ENGINE': 'postgresql_psycopg2',
	    'NAME': 'cheesely',
	    'USER': 'eleonore',
	    'HOST': '',
	    'PORT': ''
    }
}	    

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Template file locations

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# User-oploaded media files

# Defines the base URL for uploaded files
MEDIA_URL = '/media/'

# Defines which local directory the files are to be uploaded into
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Registration is open!
REGISTRATION_OPEN = True

# Select the correct user model
AUTH_USER_MODEL = "users.User"

TEMPLATE_CONTEXT_PROCESSORS = (
	# default context processors, also need to be in there,
	"django.contrib.auth.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.static",
	"django.core.context_processors.tz",
	"django.contrib.messages.context_processors.messages",

	# Add in the user's request to every template
	"django.core.context_processors.request",
)
