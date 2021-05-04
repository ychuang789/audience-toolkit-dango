"""
Django settings for audience_toolkits project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from pathlib import Path
import pymysql

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gemt7w)9ay($n(wbnj0*7t2g-f@^*q$z2-fuob)drj&0mkc=ls'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'home.apps.HomeConfig',
    'labeling_jobs.apps.LabelingJobsConfig',
    'predicting_jobs.apps.PredictingJobsConfig',
    'modeling_jobs.apps.ModelingJobsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_q',
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

ROOT_URLCONF = 'audience_toolkits.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ]
        ,
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

WSGI_APPLICATION = 'audience_toolkits.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'audience-toolkit-dango', # 目標資料庫的名稱
#         'USER': 'root', # 資料庫帳號
#         'PASSWORD': 'pohjohn88990928', # 資料庫密碼
#         'HOST': 'localhost', # 主機位置，可以先測本地localhost
#         'PORT': '3306',
#     }
# }

FILE_PATH_FIELD_DIRECTORY = 'upload_files'
MODEL_PATH_FIELD_DIRECTORY = 'model_files'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/labeling_jobs'
LOGOUT_REDIRECT_URL = '/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# tmp files
UPLOAD_FILE_DIRECTORY = 'upload_files'

# ======================================
#           django-Q settings
# ======================================
Q_CLUSTER = {
    'name': 'audience_toolkits',
    'workers': 4,
    'timeout': 10000,
    'retry': 12000,
    'queue_limit': 50,
    'bulk': 10,
    'orm': 'default'
}

# ======================================
#     ML Model Settings Task settings
# ======================================

ML_MODELS = {
    "DUMMY_MODEL": {
        'verbose_name': '假模型',
        'module': 'core.audience.models.base_model.DummyModel',
    },
    "SVM_MODEL": {
        'verbose_name': 'SVM',
        'module': 'core.audience.models.classic.svm_model.SvmModel',
    },
    "RANDOM_FOREST": {
        'verbose_name': '隨機森林',
        'module': 'core.audience.models.classic.random_forest_model.RandomForestModel',
    },
    "KEYWORD_MODEL": {
        'verbose_name': '關鍵字比對',
        'module': 'core.audience.models.rule_base.keyword_base_model.KeywordModel',
    },
}

# ======================================
#     Audience Labeler Task settings
# ======================================
# logger
VERBOSE_DEBUG_MESSAGE = True
LOG_FILE_DIRECTORY = BASE_DIR / 'logs'
LOG_BACKUP_COUNT = 30  # days
LOGGING_FORMAT = "[%(asctime)s][{_context}][%(levelname)s]: %(message)s"
LOGGING_ERROR_FORMAT = "[%(asctime)s][{_context}][%(funcName)s()][%(levelname)s]: %(message)s"

# content processing
STOP_WORD_DIR = []

# DEEPNLP APIs
DEEPNLP_POS_API = "http://rd2demo.eland.com.tw/segment"
DEEPNLP_POS_API_TOKEN = ""

# other
TEMP_DIR = BASE_DIR / 'tmp'

# predicting_result
FETCH_COUNT = -1
CONNECT_RETRIES = 3
# 若要新增AVAILABLE_FIELDS請同步調整 core.dao.input_example，key必須與InputExample對齊（會以getattr(key必須與InputExample對齊, key)取值）。
AVAILABLE_FIELDS = {
    'id': '文章id',
    's_id': '來源id',
    's_area_id': '頻道id',
    'title': '標題',
    'author': '作者',
    'content': '內文',
    'post_time': '發文時間',
}
PREDICT_DATABASE = {
    'source': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'audience-source',  # 目標資料庫的名稱
        'USER': 'root',  # 資料庫帳號
        'PASSWORD': 'password',  # 資料庫密碼
        'HOST': 'localhost',  # 主機位置，可以先測本地localhost
        'PORT': '3306',
        'SCHEMA': 'wh_bbs_01',
        'TABLE': 'ts_page_content',
    },
    'result': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'audience-result',  # 目標資料庫的名稱
        'USER': 'root',  # 資料庫帳號
        'PASSWORD': 'password',  # 資料庫密碼
        'HOST': 'localhost',  # 主機位置，可以先測本地localhost
        'PORT': '3306',
    }
}
