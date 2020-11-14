#!/usr/bin/env python

import os
import requests
import subprocess

from doodbalib import ADDONS_DIR, ADDONS_YAML, SRC_DIR, addons_config, logger

from io import BytesIO
from zipfile import ZipFile

DB_SOURCE = os.environ.get('DB_SOURCE', 'odoo')
DB_TARGET = os.environ.get('DB_TARGET', 'odoo')

PGUSER = os.environ.get('PGUSER', 'odoo')
PGPASSWORD = os.environ.get('PGPASSWORD')
PGUSER_OLD = os.environ.get('PGUSER_OLD', PGUSER)
PGPASSWORD_OLD = os.environ.get('PGPASSWORD_OLD', PGPASSWORD)

ODOO_FILESTORE_NEW = os.environ.get('ODOO_FILESTORE_NEW', '/var/lib/odoo')
ODOO_FILESTORE_OLD = os.environ.get('ODOO_FILESTORE_OLD', '/var/lib/odoo_old')
ODOO_UPDATE = os.environ.get('ODOO_UPDATE', 'all')
ODOO_SYSTEM_USER = os.environ.get('ODOO_SYSTEM_USER', 'odoo')
ODOO_SYSTEM_GROUP = os.environ.get('ODOO_SYSTEM_GROUP', 'odoo')

if os.environ.get('ODOO_DB_RESTORE') :
    
    logger.info('Setup the PostgreSQL credentials file.')
    path = '%s/.pgpass' % os.path.expanduser('~')
    with os.fdopen(os.open(path, os.O_CREAT | os.O_WRONLY, 0o600), 'w') as fh:
        fh.writelines([
            'db:5432:%s:%s:%s' % (DB_TARGET, PGUSER, PGPASSWORD),
            'db:5432:%s:%s:%s' % (DB_SOURCE, PGUSER_OLD, PGPASSWORD_OLD),
        ])
    
    logger.info('Restore the database backup into the source database.')
    logger.debug(
        subprocess.check_output(['createdb', '-h', 'db', DB_SOURCE])
    )
    logger.debug(
        subprocess.check_output(
            'psql -h db -d "%s" < %s/dump.sql' % (
                DB_SOURCE, ODOO_FILESTORE_OLD,
            ),
            shell=True,
        )
    )
    
if os.environ.get('ODOO_DB_COPY') :
    
    # (Re-)Create the target database
    try:
        logger.debug(
                subprocess.run(['dropdb', '-h', 'db', DB_TARGET])
        )
    except subprocess.CalledProcessError as e:
        print(e.output)
    logger.debug(
        subprocess.check_output(['createdb', '-h', 'db', DB_TARGET])
    )

    """Copy the backup from another database."""
    
    logger.info('Dumping the source database into the target.')
    logger.debug(
        subprocess.check_output(
            'pg_dump -h db -Fc "%s" | pg_restore -h db -d "%s"' % (
                DB_SOURCE, DB_TARGET,
            ),
            shell=True,
        )
    )
    
if os.environ.get('ODOO_FILESTORE_COPY') :
    
    logger.info('Create empty directories for the file stores if non-existent or make it empty if exists.')
    logger.info(
        subprocess.check_output([
            'mkdir', '-p',
            '%s/filestore/%s' % (ODOO_FILESTORE_NEW, DB_TARGET)
        ])
    )
    logger.info(
        subprocess.check_output([
            'rm', '-rf',
            '%s/filestore/%s' % (ODOO_FILESTORE_NEW, DB_TARGET)
        ])
    )

    logger.info('Cloning the old file store to the new one.')
    logger.debug(
        subprocess.check_output([
            'cp', '-rf',
            '%s/filestore/%s' % (ODOO_FILESTORE_OLD, DB_SOURCE),
            '%s/filestore/%s' % (ODOO_FILESTORE_NEW, DB_TARGET)
        ])
    )
    
    logger.info('Fix ownership in the new one, just in case.')
    logger.debug(
        subprocess.check_output([
            'chown', '-R',
            '%s:%s' % (ODOO_SYSTEM_USER, ODOO_SYSTEM_GROUP),
            ODOO_FILESTORE_NEW,
        ])
    )
