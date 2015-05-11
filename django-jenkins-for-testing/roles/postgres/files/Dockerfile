FROM ubuntu:14.04
MAINTAINER Kevin Glavin <archen.sol@gmail.com>

RUN locale-gen en_US.UTF-8
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
ADD pgdg.list /etc/apt/sources.list.d/pgdg.list
RUN apt-get -qq update && LC_ALL=en_US.UTF-8 DEBIAN_FRONTEND=noninteractive apt-get install -y -q postgresql-9.4 postgresql-contrib-9.4 postgresql-9.4-postgis-2.1 libpq-dev sudo python-software-properties software-properties-common

ADD postgresql.conf /etc/postgresql/9.4/main/postgresql.conf
ADD pg_hba.conf /etc/postgresql/9.4/main/pg_hba.conf
RUN chown postgres:postgres /etc/postgresql/9.4/main/*.conf

RUN sysctl -w kernel.shmmax=268435456
RUN mkdir -p /mnt/db && chown postgres:postgres /mnt/db
ADD create-postgresql-ram-tablespace.conf /etc/init/create-postgresql-ram-tablespace.conf
RUN echo 'tmpfs   /mnt/db         tmpfs   nodev,nosuid,size=2G          0  0' >> /etc/fstab

RUN apt-get clean 
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

USER postgres

RUN /etc/init.d/postgresql start &&\
    psql --command "CREATE USER jenkins SUPERUSER;" &&\
    createdb -O jenkins django &&\
    createdb -O jenkins django2 &&\
    createdb -O jenkins geodjango &&\
    createdb -O jenkins geodjango2 

RUN /etc/init.d/postgresql start &&\
    psql geodjango -c 'CREATE EXTENSION IF NOT EXISTS postgis; CREATE EXTENSION IF NOT EXISTS postgis_topology;' &&\
    psql geodjango2 -c 'CREATE EXTENSION IF NOT EXISTS postgis; CREATE EXTENSION IF NOT EXISTS postgis_topology;'

VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
EXPOSE 5432

CMD ["/usr/lib/postgresql/9.4/bin/postgres", "-D", "/var/lib/postgresql/9.4/main", "-c", "config_file=/etc/postgresql/9.4/main/postgresql.conf"]