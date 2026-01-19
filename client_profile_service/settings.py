"""
Django settings for client_profile_service project.
"""

from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv

# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Load shared .env (same across all microservices)
load_dotenv(BASE_DIR.parent / ".env")

# --------------------------------------------------
# SECURITY
# --------------------------------------------------
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "unsafe-dev-secret-key")

DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = ["*"]


# --------------------------------------------------
# APPLICATIONS
# --------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    "rest_framework_simplejwt",

    # Local app
    'profiles',
]

# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------------------------------------
# URLS & TEMPLATES
# --------------------------------------------------
ROOT_URLCONF = 'client_profile_service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'client_profile_service.wsgi.application'

# --------------------------------------------------
# DATABASE
# --------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# STATIC FILES
# --------------------------------------------------
STATIC_URL = 'static/'

# --------------------------------------------------
# MEDIA FILES (Client logos, documents)
# --------------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --------------------------------------------------
# DEFAULT PRIMARY KEY
# --------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------------------------------------
# DJANGO REST FRAMEWORK
# --------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# --------------------------------------------------
# SIMPLE JWT (SHARED ACROSS MICROSERVICES)
# --------------------------------------------------
SIMPLE_JWT = {
    'ALGORITHM': os.getenv("JWT_ALGORITHM", "HS256"),
    'SIGNING_KEY': os.getenv("JWT_SIGNING_KEY"),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
