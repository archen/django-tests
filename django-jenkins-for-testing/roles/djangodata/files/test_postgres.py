from test_sqlite3 import *  # NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'jenkins',
        'NAME': 'django',
        'TEST': {
            # ASCII_BUILD_NAME only needed on Python 2
            'NAME': 'test_django_%s_%s' % (PY_VERSION, ASCII_BUILD_NAME),
        },
    },
    'other': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'jenkins',
        'NAME': 'django2',
        'TEST': {
            'NAME': 'test_django2_%s_%s' % (PY_VERSION, ASCII_BUILD_NAME),
        },
    },
}

DATABASES = add_old_test_db_settings(DATABASES)

DEFAULT_TABLESPACE = DEFAULT_INDEX_TABLESPACE = 'ram'
