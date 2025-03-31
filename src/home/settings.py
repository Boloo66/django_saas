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


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%@wvl0@v%2@^%*nbjam51x&frc()!r39lt0iwhu4@0zski+6)t'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = os.environ.get('DJANGO_DEBUG') == True
DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ["railway.app", "https://djangosaas-production-bdc9.up.railway.app"]

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
    'commando'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
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