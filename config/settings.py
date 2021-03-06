"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's=x)3swmmcr#+r$p6ey$9%upp!l++o)^g5-glhhks^tcxgbfd6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'storages',
    'accounts',
    'photo',
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework.authtoken',
    'sample',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'layout')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sample.context_processors.language',
                # 전체 지원하는 language 목록 출력해주고,
                # 현재 language code 알려주고,
                # 언어가 어느 방향(좌,우)에서 실행되고 있는지 True, False 값으로 확인
                'django.template.context_processors.i18n',
            ],
        },
    },
]

"""
{
    'LANGUAGES' : settings.LANGUAGES,
    'LANGUAGE_CODE' : translation.get_language(),
    'LANGUAGE_BIDI' : translation.get_language_bidi(),
}
"""

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'api_dstagram_dbname',
        'USER': 'admin_wps',
        'PASSWORD': 'admin1234!',
        'HOST': 'api-dbinstance.ctj0650ag7ks.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

AWS_ACCESS_KEY_ID = 'AKIAZR3IWTCZWC4AV645'
AWS_SECRET_ACCESS_KEY = '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'
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'static-api-dstagram.wpsshool.site'
# AWS_S3_CUSTOM_DOMAIN = 's3.%s.amazonaws.com/%s' % (AWS_REGION, AWS_STORAGE_BUCKET_NAME)
AWS_S3_CUSTOM_DOMAIN = '%s' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl' : 'max-age=86400',
}
AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = 'static'
AWS_S3_SECURE_URLS = False

STATIC_URL = 'http://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'config.asset_storage.MediaStorage'

# STATIC_URL = '/static/'

"""
1) 전체 뷰에 대해서 토큰 인증방식 적용 - 일부는 제외
- settings.py에 설정 추가
2) 일부 선택해서 토큰 인증방식 적용
- 각 뷰에 인증 클래스 추가
"""

REST_FRAMEWORK = {
    # 인증해야 사용하게 해주겠다.
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # 토큰 인증방식 사용하겠다.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# Swagger UI에 토큰 기능 추가
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS':{
        'api_key':{
            'type':'apiKey',
            'name':'Authorization',
            'in':'header',
        }
    }
}

from django.utils.translation import ugettext_lazy as _
LANGUAGES = [
    ('ko', _('Korean')),
    ('en', _('English')),
]

# 번역 파일을 어디에 저장할지 설정
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

GEOIP_PATH = os.path.join(BASE_DIR, 'geoip')
