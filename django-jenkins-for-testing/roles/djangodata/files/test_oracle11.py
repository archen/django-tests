from test_sqlite3 import *  # NOQA
import test_oracle11_host as server

DJANGO_PYTHON = (BUILD_NAME.replace('.', '').replace('-', ''), PY_VERSION)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'HOST': server.HOST,
        'PORT': server.PORT,
        'NAME': server.NAME,
        'USER': 'djangotest',
        'PASSWORD': '',
        'TEST': {
            'USER': 'd_%s_%s' % DJANGO_PYTHON,
            'TBLSPACE': 'd_%s_%s' % DJANGO_PYTHON,
            'TBLSPACE_TMP': 'd_tmp_%s_%s' % DJANGO_PYTHON,
        },
    },
    'other': {
        'ENGINE': 'django.db.backends.oracle',
        'HOST': server.HOST,
        'PORT': server.PORT,
        'NAME': server.NAME,
        'USER': 'djangotest',
        'PASSWORD': '',
        'TEST': {
            'USER': 'd2_%s_%s' % DJANGO_PYTHON,
            'TBLSPACE': 'd2_%s_%s' % DJANGO_PYTHON,
            'TBLSPACE_TMP': 'd2_tmp_%s_%s' % DJANGO_PYTHON,
        },
    },
}

DATABASES = add_old_test_db_settings(DATABASES)
