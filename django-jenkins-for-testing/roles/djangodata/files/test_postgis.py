from test_sqlite3 import *  # NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'jenkins',
        'NAME': 'geodjango',
        'TEST': {
            # ASCII_BUILD_NAME only needed on Python 2
            'NAME': 'test_django_gis_%s_%s' % (PY_VERSION, ASCII_BUILD_NAME),
        },
    },
    'other': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'jenkins',
        'NAME': 'geodjango2',
        'TEST': {
            'NAME': 'test_django2_gis_%s_%s' % (PY_VERSION, ASCII_BUILD_NAME),
        },
    },
}

DATABASES = add_old_test_db_settings(DATABASES)

DEFAULT_TABLESPACE = DEFAULT_INDEX_TABLESPACE = 'ram'
