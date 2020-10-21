#!/usr/bin/env python

import os
import requests
import subprocess

from doodbalib import ADDONS_DIR, ADDONS_YAML, SRC_DIR, addons_config, logger as logging

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

if os.environ.get('DB_SOURCE') :
    
    logging.info('FIX mail_message_res_partner_needaction_rel.')
    logging.debug(
        subprocess.check_output(
            'psql -h db -d "%s" -c "delete from mail_message_res_partner_needaction_rel where mail_message_id not in (select id from mail_message);"' % (
                DB_SOURCE,
            ),
            shell=True,
        )
    )
    logging.debug(
        subprocess.check_output(
            'psql -h db -d "%s" -c "delete from mail_message_res_partner_needaction_rel where res_partner_id not in (select id from res_partner);"' % (
                DB_SOURCE, 
            ),  
            shell=True,
        )   
    )   