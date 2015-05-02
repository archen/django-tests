import os
import platform
import sys

from test_sqlite import *  # NOQA

PY_VERSION = os.environ.get('PY_VERSION', 'unknown')
# this is set by runtests_jenkins.sh; it's something like 'django-master'.
BUILD_NAME = os.environ['BUILD_NAME']
DATABASE = os.environ.get('database', '')
# executor number is zero indexed
EXECUTOR_NUMBER = int(os.environ.get('EXECUTOR_NUMBER'))

memcached_port = 11211 + EXECUTOR_NUMBER

if sys.version_info[0] == 2:
    ASCII_BUILD_NAME = BUILD_NAME.decode('ascii', 'ignore')
else:
    ASCII_BUILD_NAME = BUILD_NAME.encode('ascii', 'ignore')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'memcached': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:%s' % memcached_port,
        'KEY_PREFIX': '%s_%s_%s' % (PY_VERSION, DATABASE, ASCII_BUILD_NAME),
    }
}


def add_old_test_db_settings(DATABASES):
    # Add the TEST_ version of the database test settings based on the
    # test dictionary. Remove when only Django >= 1.7 is supported.
    for db_alias, db_settings in DATABASES.items():
        if 'TEST' in db_settings:
            for test_key, test_value in db_settings['TEST'].items():
                DATABASES[db_alias]['TEST_' + test_key] = test_value
    return DATABASES
