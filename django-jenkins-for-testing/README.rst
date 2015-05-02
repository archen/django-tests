================================
Django Jenkins Ansible Playbooks
================================

Getting Started
===============

After you clone this repository, you'll need to download some files from
http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html and put
them in roles/oracle-client/files (in .gitignore so they won't be committed):

* instantclient-sdk-linux.x64-11.2.0.4.0.zip
* oracle-instantclient11.2-basiclite-11.2.0.4.0-1.x86_64.rpm

We do this to avoid storing large binary blobs in source control.

Configuring the master
======================

The machine
-----------

The master is accessible at (jenkins.djangoproject.com).

It's an "8GB Performance" node hosted at Rackspace.

It's running Ubuntu 12.04 because the builds for Django 1.4-1.7 aren't
compatible with 14.04, so this provides a place to run those builds.
Various issues:

* The PostGIS packages in 14.04 are not compatible with Django 1.4.
* The included version of Python 3.2 (3.2.6) has issues; http://bugs.python.org/issue22758

Once only Django 1.8+ are supported, we can probably upgrade this machine.

It should be in the "Jenkins CI Cluster" virtual network (in Rackspace UI) so
it can access the Oracle database server.

Auxiliary disk
--------------

A 500 GB auxiliary disk is mounted as ``/mnt/jenkinsdata/`` which holds the
build data.

This requires some manual configuration outside of the ansible playbooks.

First, format the as described in the `Rackspace KB
<http://www.rackspace.com/knowledge_center/article/prepare-your-cloud-block-storage-volume>`.

Then run these steps to mount the device:

    mkdir -p /mnt/jenkinsdata/
    mount /dev/xvdb1 /mnt/jenkinsdata/
    chown jenkins:jenkins /mnt/jenkinsdata/

Add it to ``/etc/fstab`` to make the mount permanent:

    /dev/xvdb1 /mnt/jenkinsdata ext4 defaults,noatime,_netdev,nofail 0 2

Then tell Jenkins to use the new directory:

    Jenkins UI -> Manage Jenkins -> Configure System -> Advanced

    Workspace Root Directory: /mnt/jenkinsdata/workspace/${ITEM_FULLNAME}
    Build Record Root Directory: /mnt/jenkinsdata/builds/${ITEM_FULLNAME}

Running a playbook
------------------

First, bootstrap the users on the machine (this requires the machine to be
created with your public key so it's in authorized_keys of the root user):

    ansible-playbook -i hosts -l master bootstrap_users.yml -u root

Now, you can run the playbook like this:

    ansible-playbook -i hosts -l master deploy.yml -u timgraham

The complete list of playbooks should be idempotent so you can run them at any
time, but I'd recommend only running the role you are modifying by commenting
out the others in deploy.yml so things don't take so long. There are a couple
things that could be improved like in the python role, wheel files are
regenerated on each run even if they already exist.

Adding a slave
==============

The machines
------------

All slaves run Ubuntu 14.04; see the "trusty" branch of this repository to
run the playbooks for them. The machines are "8 GB General Purpose v1"
(replaces "Performance" nodes).

They should be in the "Jenkins CI Cluster" virtual network (in Rackspace UI) so
they can access the Oracle database server.

Running a playbook
------------------

After bootstrapping the users as described above, you can run the playbook
on the slaves like this:

    ansible-playbook -i hosts -l slaves deploy.yml -u timgraham

You'll probably get an error about MySQL failing to restart. At this point,
simply reboot the server and it should be ready to go.

Add the node in Jenkins master UI
---------------------------------

http://djangoci.com/computer/new
Node name: ciN
* Dumb slave

# of executors: 8 (the node has 8 vCPUs)
Remote FS root: /home/jenkins
Host: ciN.djangoproject.com
Credentials: jenkins

For Ubuntu 14.04:
Labels: trusty
Usage: Only build jobs with label restrictions matching this node

Oracle
======

The machine
-----------

The machine is accessible at 162.242.226.85 (ci3.dp.com).

It's an "4GB Performance" node hosted at Rackspace. Unlike the other nodes,
it's running CentOS (for compatibility with Oracle).

Running a playbook
------------------

Most of the configuration was done manually by Shai as Oracle installation
requires manual intervention and cannot be automated.

Some configuration is automated (IP tables as of this writing). You can run
the playbook on the Oracle servers like this:

    ansible-playbook -i hosts -l oracle deploy.yml --ask-sudo
