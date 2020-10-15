#!/usr/bin/env python

import logging
import os
import requests
import subprocess

from io import BytesIO
from zipfile import ZipFile

DB_SOURCE = os.environ.get('DB_SOURCE', 'odoo')

PGUSER = os.environ.get('PGUSER', 'odoo')
PGPASSWORD = os.environ.get('PGPASSWORD')

ODOO_FILESTORE = os.environ.get('ODOO_FILESTORE_NEW', '/var/lib/odoo')
ODOO_UPDATE = os.environ.get('ODOO_UPDATE', 'all')
ODOO_SYSTEM_USER = os.environ.get('ODOO_SYSTEM_USER', 'odoo')
ODOO_SYSTEM_GROUP = os.environ.get('ODOO_SYSTEM_GROUP', 'odoo')

logging.info('Copying the database backup into the target database.')
logging.debug(
    subprocess.check_output(
        'psql -h db -d "%s" < %s/dump.sql' % (
            DB_SOURCE, ODOO_FILESTORE,
        ),
        shell=True,
    )
)

logging.debug(
    subprocess.check_output([
        'chown', '-R',
        '%s:%s' % (ODOO_SYSTEM_USER, ODOO_SYSTEM_GROUP),
        ODOO_FILESTORE,
    ])
)