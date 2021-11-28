#!/usr/bin/env python

import os
import requests
import subprocess

try:
    from subprocess import CompletedProcess
except ImportError:
    # Python 2


    class CompletedProcess:

        def __init__(self, args, returncode, stdout=None, stderr=None):
            self.args = args
            self.returncode = returncode
            self.stdout = stdout
            self.stderr = stderr

        def check_returncode(self):
            if self.returncode != 0:
                err = subprocess.CalledProcessError(self.returncode, self.args, output=self.stdout)
                raise err
            return self.returncode

    def sp_run(*popenargs, **kwargs):
        input = kwargs.pop("input", None)
        check = kwargs.pop("handle", False)
        if input is not None:
            if 'stdin' in kwargs:
                raise ValueError('stdin and input arguments may not both be used.')
            kwargs['stdin'] = subprocess.PIPE
        process = subprocess.Popen(*popenargs, **kwargs)
        try:
            outs, errs = process.communicate(input)
        except:
            process.kill()
            process.wait()
            raise
        returncode = process.poll()
        if check and returncode:
            raise subprocess.CalledProcessError(returncode, popenargs, output=outs)
        return CompletedProcess(popenargs, returncode, stdout=outs, stderr=errs)

    subprocess.run = sp_run
    # ^ This monkey patch allows it work on Python 2 or 3 the same way

from doodbalib import ADDONS_DIR, ADDONS_YAML, SRC_DIR, addons_config, logger

from io import BytesIO
from zipfile import ZipFile

DB_SOURCE = os.environ.get('DB_SOURCE', 'odoo')

PGUSER = os.environ.get('PGUSER', 'odoo')
PGPASSWORD = os.environ.get('PGPASSWORD')

ODOO_FILESTORE_NEW = os.environ.get('ODOO_FILESTORE_NEW', '/var/lib/odoo')
ODOO_UPDATE = os.environ.get('ODOO_UPDATE', 'all')
ODOO_SYSTEM_USER = os.environ.get('ODOO_SYSTEM_USER', 'odoo')
ODOO_SYSTEM_GROUP = os.environ.get('ODOO_SYSTEM_GROUP', 'odoo')

if os.environ.get('ODOO_DB_RESTORE') :
    
    logger.info('Setup the PostgreSQL credentials file.')
    path = '%s/.pgpass' % os.path.expanduser('~')
    with os.fdopen(os.open(path, os.O_CREAT | os.O_WRONLY, 0o600), 'w') as fh:
        fh.writelines([
            'db:5432:%s:%s:%s' % (DB_SOURCE, PGUSER, PGPASSWORD),
        ])
    
    logger.info('Restore the database backup into the source database.')
    logger.debug(
        subprocess.run(['dropdb', '-h', 'db', DB_SOURCE])
    )
    logger.debug(
        subprocess.check_output(['createdb', '-h', 'db', DB_SOURCE])
    )
    logger.debug(
        subprocess.check_output(
            'psql -h db -d "%s" < %s/dump.sql' % (
                DB_SOURCE, ODOO_FILESTORE_NEW,
            ),
            shell=True,
        )
    )
    
if os.environ.get('ODOO_DB_COPY') :
    
    # (Re-)Create the target database
    logger.debug(
        subprocess.run(['dropdb', '-h', 'db', DB_TARGET])
    )
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