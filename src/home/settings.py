"""
Django settings for home project.

Generated by 'django-admin startproject' using Django 5.0.13.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from decouple import config
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

EMAIL_HOST=config('EMAIL_HOST', cast=str, default='smtp.gmail.com')
EMAIL_PORT=config('EMAIL_PORT', cast=str, default="587")
EMAIL_HOST_USER=config('EMAIL_HOST_USER', cast=str, default=None)
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD', cast=str, default=None)
EMAIL_USE_TLS=config('EMAIL_USE_TLS', cast=bool, default=True)
EMAIL_USE_SSL=config('EMAIL_USE_SSL', cast=bool, default=False) #465
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ADMIN_USER_NAMES = config('ADMIN_USER_NAMES', cast=lambda v: v.split(','), default="")
ADMIN_USER_EMAILS = config('ADMIN_USER_EMAILS', cast=lambda v: v.split(','), default="")

ADMINS = []

if ADMIN_USER_NAMES and ADMIN_USER_EMAILS and len(ADMIN_USER_NAMES) == len(ADMIN_USER_EMAILS):
    ADMINS.extend(zip(
        [name.strip('"').strip() for name in ADMIN_USER_NAMES], 
        [email.strip('"').strip() for email in ADMIN_USER_EMAILS]  
    ))
    MANAGERS = ADMINS.copy()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%@wvl0@v%2@^%*nbjam51x&frc()!r39lt0iwhu4@0zski+6)t'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = os.environ.get('DJANGO_DEBUG') == True
DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ["railway.app", "djangosaas-production-bdc9.up.railway.app"]

if DEBUG:
    ALLOWED_HOSTS += ["127.0.0.1", "localhost"]
    ALLOWED_HOSTS.append("*")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #my apps
    'commando',
    'user_auth',

    #3rd party libraries
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    "allauth.account.middleware.AccountMiddleware",
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'home.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'home.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASE_URI=config("DATABASE_URI", default=None,)

if DATABASE_URI is not None:
    import dj_database_url
    DATABASES['default'] = dj_database_url.config(default=DATABASE_URI, conn_max_age=600, conn_health_checks=True)

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#djang0-allauth configurations
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_LOGIN_METHODS = {'email', 'username'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']
LOGIN_REDIRECT_URL = '/'

# Email configurations
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_PREVENT_ENUMERATION = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[DJango-SaaS] '

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

CSRF_TRUSTED_ORIGINS = ["https://railway.app", "https://djangosaas-production-bdc9.up.railway.app"]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_BASE_DIR = BASE_DIR / 'static'
STATICFILES_VENDOR_DIR = STATICFILES_BASE_DIR / 'vendors'
STATICFILES_VENDOR_DIR.mkdir(parents=True, exist_ok=True)

# sources(s) for python manage.py collectstatic
STATICFILES_DIRS = [
    STATICFILES_BASE_DIR,
    STATICFILES_VENDOR_DIR
]

#outputs(s) for python manage.py collectstatic
STATIC_ROOT = BASE_DIR.parent / 'local_cdn'

# if not DEBUG:
#     STATIC_ROOT = BASE_DIR / 'prod_cdn'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR /'media'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {}