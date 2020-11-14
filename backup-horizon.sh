#!/bin/bash
# vars
BACKUP_DIR=~/migration
ODOO_DATABASE=horizon
ADMIN_PASSWORD=$ADMIN_PASSWORD
# create a backup directory
cd ${BACKUP_DIR}
# create a backup
curl -X POST \
    -F "master_pwd=${ADMIN_PASSWORD}" \
    -F "name=${ODOO_DATABASE}" \
    -F "backup_format=zip" \
    -o ${BACKUP_DIR}/backup.zip \
    https://horizon.student-crlg.be/web/database/backup