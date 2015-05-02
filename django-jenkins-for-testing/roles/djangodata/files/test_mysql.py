from test_sqlite3 import *  # NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'django',
        'PASSWORD': '',
        'NAME': 'django',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
        },
        'TEST': {
            'NAME': 'test_django_%s_%s' % (PY_VERSION, ASCII_BUILD_NAME),
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        },
    },
    'other': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'django',
        'PASSWORD': '',
        'NAME': 'django2',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
        },
        'TEST': {
            'NAME': 'test_django2_%s_%s' % (PY_VERSION, ASCII_BUILD_NAME),
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        },
    },
}

DATABASES = add_old_test_db_settings(DATABASES)
