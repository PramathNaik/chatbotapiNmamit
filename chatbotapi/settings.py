"""
Django settings for chatbotapi project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
import django_heroku
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cgkcx0z6dr^y$i_9pvm4pv@4)cjehdu4x!gtgx(wc-38x8&7e_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'main',
    'feedback',
    'keywords',
    'rest_framework',
    'simple_chatbot',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chatbotapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'chatbotapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SIMPLE_CHATBOT = {
    'responses': (
        ("main.responses.GreetingResponse", "Greeting"),
        ("main.responses.GoodbyeResponse", "Goodbye"),
        ("main.responses.LocatedResponse","location"),
        ("main.responses.establishedResponce","established"),
        ("main.responses.nirfrank","nirf"),
        ("main.responses.founder","founder"),
        ("main.responses.Principle","Principle"),
        ("main.responses.website","website"),
        ("main.responses.distMangalore","distMangalore"),
        ("main.responses.Alumnis","Alumnis"),
        ("main.responses.officialMail","officialMail"),
        ("main.responses.girlsHostel","girlsHostel"),
        ("main.responses.boysHostel","boysHostel"),
        ("main.responses.TransportationFacilities","TransportationFacilities"),
        ("main.responses.CanteenFacilities","CanteenFacilities"),
        ("main.responses.HealthcareFacilities","HealthcareFacilities"),
        ("main.responses.contactNumber","contactNumber"),
        ("main.responses.CampusContacts","CampusContacts"),
        ("main.responses.Btechprogrammes","Btechprogrammes"),
        ("main.responses.CompaniesNo","CompaniesNo"),
        ("main.responses.HighestPackage","HighestPackage"),
        ("main.responses.studentsPlaced","studentsPlaced"),
        ("main.responses.averagePackage","averagePackage"),
        ("main.responses.placementsUpdates","placementsUpdates"),
        ("main.responses.placementTrainingName","placementTrainingName"),
        ("main.responses.PlacementHead","PlacementHead"),
        ("main.responses.QualificationPlacementHead","QualificationPlacementHead"),
        ("main.responses.ContactPlacement","ContactPlacement"),
        ("main.responses.cgpaPlacement","cgpaPlacement"),
        ("main.responses.cgpasuperdream","cgpasuperdream"),
        ("main.responses.recruitmentPolicy","recruitmentPolicy"),
        ("main.responses.ProgramsAvailable","ProgramsAvailable"),
        ("main.responses.CoursesAvailablePostgraduate","CoursesAvailablePostgraduate"),
        ("main.responses.CoursesAvailableDoctoral","CoursesAvailableDoctoral"),
        ("main.responses.CoursesAvailableBTECH","CoursesAvailableBTECH"),
        ("main.responses.CoursesAvailableMTECH","CoursesAvailableMTECH"),
        ("main.responses.eligibilitycriteriaBTECH","eligibilitycriteriaBTECH"),
        ("main.responses.admissionprocedureBTECH","admissionprocedureBTECH"),
        ("main.responses.generalcategoryBTECH","generalcategoryBTECH"),
        ("main.responses.NRIcategoryBTECH","NRIcategoryBTECH"),
        ("main.responses.classescommence","classescommence"),
        ("main.responses.accommodation","accommodation"),
        ("main.responses.foodfacilities","foodfacilities"),
        ("main.responses.Feestructure","Feestructure"),
        ("main.responses.scholarshipcategory","scholarshipcategory"),
        ("main.responses.generalcategory","generalcategory"),
        ("main.responses.NRIcategory","NRIcategory"),
        ("main.responses.libraryfacilities","libraryfacilities"),
        ("main.responses.Hostelfacilities","Hostelfacilities"),
        ("main.responses.facultymembersoftheplacementdepartment","facultymembersoftheplacementdepartment"),
        ("main.responses.websiteregardingplacements","websiteregardingplacements"),
        ("main.responses.emailidoftheplacementdepartment","emailidoftheplacementdepartment"),
        ("main.responses.placementsessionusuallystart","placementsessionusuallystart"),
        ("main.responses.activitiesconducted","activitiesconducted"),
        ("main.responses.WhatNmamit","WhatNmamit"),
    ),
}
STATIC_ROOT = os.path.join(BASE_DIR,"static")
django_heroku.settings(locals())
#STATICFILES_DIRS = [os.path.join(BASE_DIR,"static"),]