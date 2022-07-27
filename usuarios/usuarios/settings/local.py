#El entorno local es el entorno que hacemos aqui, dentro de nuestro computador

#Al igual que en base.py , pegamos todo lo que hay dentro de settings.py y luego
#eliminamos todo aquello que ya tenemos en base.py


# SECURITY WARNING: don't run with debug turned on in production!

#es necersario importar todas las configuraciones de base.py
from .base import *
from pathlib import Path
DEBUG = True


ALLOWED_HOSTS = []



# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER':get_secret('USER'),
        'PASSWORD':get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
STATIC_URL = '/static/'
#es el BASE_DIR de base.py. Le indicamos que dentro de la raiz busque entre sus hijos
#la carpeta llamada static
STATICFILES_DIRS=[BASE_DIR.child('static')]
#MEDIA_URL='/media/'
#que busque denmtro de la estructura base la carpeta 'media'
#MEDIA_ROOT=BASE_DIR.child('media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
