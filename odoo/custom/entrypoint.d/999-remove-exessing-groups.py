#!/usr/bin/env python

import os
import requests
import subprocess

from doodbalib import ADDONS_DIR, ADDONS_YAML, SRC_DIR, addons_config, logger

from io import BytesIO
from zipfile import ZipFile

DB_TARGET = os.environ.get('DB_TARGET', 'odoo')

if os.environ.get('DB_TARGET') :
    
    logger.info('FIX res_groups_users_rel group 12.')
    logger.debug(
        subprocess.check_output(
            'psql -h db -d "%s" -c "DELETE FROM res_groups_users_rel where gid = 12;"' % (
                DB_TARGET,
            ),
            shell=True,
        )
    )
    
    logger.info('FIX res_groups_users_rel group 13.')
    logger.debug(
        subprocess.check_output(
            'psql -h db -d "%s" -c "DELETE FROM res_groups_users_rel where gid = 13;"' % (
                DB_TARGET,
            ),
            shell=True,
        )
    )