from test_sqlite3 import *  # NOQA
import test_oracle11_host as server

DJANGO_PYTHON = (BUILD_NAME.replace('.', '').replace('-', ''), PY_VERSION)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.oracle',
        'HOST': server.HOST,
        'PORT': server.PORT,
        'NAME': server.NAME,
        'USER': 'djangotest',
        'PASSWORD': '',
        'TEST': {
            'USER': 'g_%s_%s' % DJANGO_PYTHON,
            'TBLSPACE': 'g_%s_%s' % DJANGO_PYTHON,
            'TBLSPACE_TMP': 'g_tmp_%s_%s' % DJANGO_PYTHON,
        }
    },
    'other': {
        'ENGINE': 'django.contrib.gis.db.backends.oracle',
        'HOST': server.HOST,
        'PORT': server.PORT,
        'NAME': server.NAME,
        'USER': 'djangotest',
        'PASSWORD': '',
        'TEST': {
            'USER': 'g2_%s_%s' % DJANGO_PYTHON,
            'TBLSPACE': 'g2_%s_%s' % DJANGO_PYTHON,
            'TBLSPACE_TMP': 'g2_tmp_%s_%s' % DJANGO_PYTHON,
        }
    },
}

DATABASES = add_old_test_db_settings(DATABASES)
