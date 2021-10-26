import os
import dj_database_url
from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!

if "NO_TEST" in os.environ:
    # HEROKU
    SECRET_KEY = os.environ.get("SECRET_KEY", "")
else:
    # LOCAL
    SECRET_KEY = os.environ.get("SECRET_KEY", "test")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if "NO_TEST" in os.environ:
    ALLOWED_HOSTS = ["yoga-app-django-m4.herokuapp.com"]  # heroku
else:
    ALLOWED_HOSTS = []  # local

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    # Third party apps
    "crispy_forms",
    "storages",

    # My apps
    "pages.apps.PagesConfig",
    "courses.apps.CoursesConfig",
    "teachers.apps.TeachersConfig",
    "accounts.apps.AccountsConfig",
    "contacts.apps.ContactsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "yoga_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "yoga_app.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


if "NO_TEST" in os.environ:
    DATABASES = {
        # HEROKU
        "default": dj_database_url.parse(
            "postgres://cvjbpbpbddjdru:9ed25d74ecebbc2df2e5915daeb8124a8ae8327f7ffb2cbc3e695c10aadb661b@ec2-52-209-134-160.eu-west-1.compute.amazonaws.com:5432/dfoaf5fg4no4mg"
        )
    }
else:
    DATABASES = {
        # LOCAL
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "yogaapp",
            "USER": "postgres",
            "PASSWORD": "password1",
            "HOST": "localhost",
            "PORT": "9001",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# MESSAGES
MESSAGE_TAGS = {messages.ERROR: "danger"}

if 'EMAIL_DEV' in os.environ:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_PORT = 587
    EMAIL_HOST_USER = os.environ.get("EMAIL_USER1")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS1")
    EMAIL_USE_TLS = True
else:
    # EMAIL CONFIG
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_PORT = 587
    EMAIL_HOST_USER = "test@gmail.com"
    EMAIL_HOST_PASSWORD = "fakepass"
    EMAIL_USE_TLS = True

CRISPY_TEMPLATE_PACK = "bootstrap4"

LOGIN_URL = "/accounts/login"
LOGIN_REDIRECT_URL = "/accounts/dashboard"
LOGOUT_REDIRECT_URL = "/"

# Static files(CSS, JavaScript, Images)
# https: // docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "yoga_app/static")]

# Media folder settings
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# S3 BUCKET CONFIG
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'yoga_app/static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

# Stripe Credentials
STRIPE_PUBLISHABLE_KEY = os.getenv(
    'STRIPE_PUBLISHABLE_KEY', '')
STRIPE_SECRET_KEY = os.getenv(
    'STRIPE_SECRET_KEY', '')
STRIPE_WEBHOOK_SECRET = os.getenv(
    'STRIPE_WEBHOOK_SECRET', '')

['OBJECT_NAME', 'ReprJSONEncoder', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__',
 '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
 '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__',
 '__setitem__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_last_response',
 '_previous',
 '_retrieve_params', '_static_request', '_static_request_stream', '_transient_values', '_unsaved_values', 'api_base',
 'api_key', 'auto_paging_iter', 'class_url', 'clear', 'construct_from', 'copy', 'create', 'fromkeys', 'get',
 'instance_url', 'items', 'keys', 'last_response', 'line_items_request', 'line_items_url', 'list', 'list_line_items',
 'pop', 'popitem', 'refresh', 'refresh_from', 'request', 'request_stream', 'retrieve', 'serialize', 'setdefault',
 'stripe_account', 'stripe_id', 'stripe_version', 'to_dict', 'to_dict_recursive', 'update', 'values']
