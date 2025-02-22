from email.policy import default
from pathlib import Path
import os
import django.contrib
import django.contrib.staticfiles
import django.contrib.staticfiles.storage


BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------
# Setup Environmental Variables
import environ

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# ENVIRONMENT = env('DJANGO_ENV', default = 'development')
# if ENVIRONMENT == 'production':
#     environ.Env.read_env(os.path.join(BASE_DIR, '.env.de'))
# else:
#     environ.Env.read_env(os.path.join(BASE_DIR, '.env.prod'))
    
# ----------------------------------------------------------
DEBUG = env('DEBUG', default=False)
ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS').split(',')

SECRET_KEY = env('DJANGO_SECRET_KEY')
# ------------------------------------------------------------------------

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # whitenoise
    "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',
    # allauth requirement
    'django.contrib.sites',
    # local
    'accounts',
    'app_pages',
    'app_blogs',
    
    # third-party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    "crispy_forms",
    "crispy_bootstrap5",
    "debug_toolbar",
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # allauth account middleware:
    "allauth.account.middleware.AccountMiddleware",
    # django debug toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # whitenoise
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'blog_project.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'blog_project.wsgi.application'



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'HOST': 'db',
#         'PORT': 5432
#     }
# }
DATABASES = {
    'default': env.db()
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR,]
# For collectstatic in production:
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -------------------------------------------------------------------------
# Media Configuration
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# --------------------------------------------------------------------------------------------
# Crispy Form
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CustomUser
AUTH_USER_MODEL = "accounts.CustomUser"

# ------------------------------------------------------------------------------------
# django allauth config
SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
ACCOUNT_SESSION_REMEMBER = True
LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT = "home"

# ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"
# ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"
# SOCIALACCOUNT_ADAPTER = "allauth.socialaccount.adapter.DefaultSocialAccountAdapter"


# Email Authentication and authorization
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_UNIQUE = True
# Single password only
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

# Verification of email when signing up
ACCOUNT_EMAIL_VERIFICATION = "optional"
# SOCIALACCOUNT_ENABLED = False
# SOCIALACCOUNT_EMAIL_VERIFICATION = "none"


# ---------------------------------------------------------------------------------------------
# Email Configurations
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('DJANGO_EMAIL_HOST')
EMAIL_PORT = env('DJANGO_EMAIL_PORT')
EMAIL_USE_TLS = env('DJANGO_EMAIL_USE_TLS')
EMAIL_HOST_USER = env('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('DJANGO_EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')


# django debug toolbar
import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]


# Deployment Checklist
SECURE_SSL_REDIRECT=env.bool('DJANGO_SECURE_SSL_REDIRECT', default=False)
SECURE_HSTS_SECONDS=env.int('DJANGO_SECURE_HSTS_SECONDS', default=0)
SECURE_HSTS_INCLUDE_SUBDOMAINS=env.bool('DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', default=False)
SECURE_HSTS_PRELOAD=env.bool('DJANGO_SECURE_HSTS_PRELOAD', default=False)
SESSION_COOKIE_SECURE=env.bool('DJANGO_SESSION_COOKIE_SECURE', default=False)
CSRF_COOKIE_SECURE=env.bool('DJANGO_CSRF_COOKIE_SECURE', default=False)




CSRF_TRUSTED_ORIGINS = [
    "http://13.203.102.141:8080",
    "http://127.0.0.1:8080",
    "http://localhost:8080",
    "http://ec2-13-203-102-141.ap-south-1.compute.amazonaws.com:8080",
]