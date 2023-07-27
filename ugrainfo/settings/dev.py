from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-8+(fgey3gfk39v390_%c%_h9tf4cii@as+p8a_9+$lf9uka5w1"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['testug.ra','www.testug.ra.com','51.250.29.164','127.0.0.1', 'localhost']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
