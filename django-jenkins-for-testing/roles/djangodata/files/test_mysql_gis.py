from test_sqlite3 import *  # NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'USER': 'django',
        'PASSWORD': '',
        'NAME': 'django_gis',
        'OPTIONS': {
            'init_command': 'SET storage_engine=MyISAM',
        },
        'TEST': {
            'NAME': 'test_django_gis_%s_%s' % (PY_VERSION, ASCII_BUILD_NAME),
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        },
    },
    'other': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'USER': 'django',
        'PASSWORD': '',
        'NAME': 'django2_gis',
        'OPTIONS': {
            'init_command': 'SET storage_engine=MyISAM',
        },
        'TEST': {
            'NAME': 'test_django2_gis_%s_%s' % (PY_VERSION, ASCII_BUILD_NAME),
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        },
    },
}

DATABASES = add_old_test_db_settings(DATABASES)
