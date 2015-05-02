# Jenkins runs the shell with -e, but we don't want to exit
# without cleaning up.
set +e

export django_admin=../django/bin/django-admin.py
export TMPDIR=`mktemp -d -t jenkins.XXXXXXXXXX`
export PYTHONPATH=..:.
export BUILD_NAME="$(echo "$JOB_NAME" | cut -d '/' -f 1)"
export PY_VERSION=`echo $python | sed -n 's/py.*\([0-9]\)\.\([0-9]\)/\1\2/p'`
export PY_MAJOR_VERSION=`echo $PY_VERSION | cut -b 1`
export DJANGO_LIVE_TEST_SERVER_ADDRESS=localhost:8081-8099
alias PIP_INSTALL='pip install --no-index -f ~/wheelhouse/'
test_apps=''  # by default run all tests

echo "**> creating virtualenv"
virtualenv .env -p /usr/bin/$python
. .env/bin/activate
echo "**> installing requirements"

PIP_INSTALL -r requirements/py$PY_MAJOR_VERSION.txt

if [ -f "requirements/$database.txt" ]; then
  PIP_INSTALL -r requirements/$database.txt
fi

if [ "$database" = 'postgis' ]; then
  PIP_INSTALL -r requirements/postgres.txt
fi

if [ "$database" = 'mysql_gis' ]; then
  PIP_INSTALL -r requirements/mysql.txt
  test_apps='django.contrib.gis'
fi

if [ "$database" = "oracle11" ] || [ "$database" = "oragis11" ]; then
  PIP_INSTALL -r requirements/oracle.txt
  . .env/bin/activate
  . ./$database.env
  if [ "$database" = "oragis11" ]; then
    test_apps='django.contrib.gis'
  fi
fi

if [ "$database" = 'spatialite' ]; then
  PIP_INSTALL pysqlite
fi

if [ "$test_apps" = 'django.contrib.gis' ]; then
  # Django 1.4
  if [ "$BUILD_NAME" = 'django-1.4' ]; then
    test_apps='gis'
  fi

  # Django 1.8+
  if [ -d 'gis_tests' ]; then
    test_apps='gis_tests'
  fi
fi

$python -Wall ./runtests.py $test_apps --verbosity 2 --settings=test_$database --noinput $EXTRA_RUNTESTS_ARGS
retcode=$?

rm -rf $TMPDIR
exit $retcode
