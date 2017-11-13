import os

# ===
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/
# SECURITY WARNING: don't run with debug turned on in production!
# ===
ADMINS = (('Dani Roxberry', 'dani@bitoriented.com'), )
DEBUG = True
ALLOWED_HOSTS = ['*']


# ===
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
# ===

PROJECT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'templates')
        ],
    }
]

# ===
# django-compressor
# ===
COMPRESS_ENABLED = False
COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT
STATICFILES_FINDERS = ['compressor.finders.CompressorFinder']

# ===
# Apps
# ===
INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    # 3rd Party
    'social_django',
    'compressor',
    'randomslugfield',

    # Custom
    'core.app',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# ===
# django_social
# ===
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

SOCIAL_AUTH_STRATEGY = 'social_django.strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social_django.models.DjangoStorage'
SOCIAL_AUTH_EMAIL_FORM_HTML = 'email_signup.html'
SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'app.mail.send_validation'
SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/email-sent/'
SOCIAL_AUTH_USERNAME_FORM_HTML = 'username_signup.html'


# ===
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# ===
DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
    }
}

# ===
# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
# ===
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

# ===
# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/
# ===
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ===
# Celery
# ===
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'



# ===
# r3 specific settings
# ===
SOCKJS_PORT = 7888
SITE_DOMAIN = 'r3view.dev'
WS_URL = '//{}:{}/echo'.format(SITE_DOMAIN, SOCKJS_PORT)

# ===
# GitHub oAuth integration
# ===
GITHUB_REDIRECT = 'https://github.com/login/oauth/authorize'
GITHUB_REDIRECT_EXCHANGE = 'https://github.com/login/oauth/access_token'
GITHUB_API = 'https://api.github.com/user'
SOCIAL_AUTH_GITHUB_KEY = ''
SOCIAL_AUTH_GITHUB_SECRET = ''
REDIRECT_URL = ''

# ===
# Load up local_settings.py --- omitted from git!
# Should only exist on your local machine.
# ===
try:
    from core.local_settings import *
except:
    pass
