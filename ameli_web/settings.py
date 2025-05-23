"""
Django settings for ameli_web project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# === Chemin de base du projet ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === Gestion des fichiers médias (Excel générés) ===
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'document')

# === Paramètres de sécurité ===
SECRET_KEY = 'django-insecure-=-fqn=2)gq@n35c*r#%ttvykv%$7p^lqqa-hz40-v3v(0$qiw_'
DEBUG = True
ALLOWED_HOSTS = ['ameli-backend.onrender.com', 'localhost', '127.0.0.1']


# === Applications Django + DRF + CORS + app perso ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'extract',
    'rest_framework',
    'corsheaders',
]

# === Middleware ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# === Fichier racine des routes URL ===
ROOT_URLCONF = 'ameli_web.urls'

# === Configuration des templates ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# === Application WSGI ===
WSGI_APPLICATION = 'ameli_web.wsgi.application'

# === Base de données SQLite par défaut ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# === Validation des mots de passe ===
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

# === Langue et fuseau horaire ===
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# === Fichiers statiques (CSS, JS, etc.) ===
STATIC_URL = 'static/'

# === Clé primaire par défaut ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# === Autoriser toutes les origines pour les appels frontend (ex: GitHub Pages) ===
CORS_ALLOWED_ORIGINS = [
    "https://Osatch.github.io",
]

