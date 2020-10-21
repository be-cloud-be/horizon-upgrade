#!/usr/bin/env python
from __future__ import print_function
import click

import click_odoo

@click.command()
@click_odoo.env_options(default_log_level='error')
def main(env):
    print 'DROP v9c_backend_theme'
    env['ir.module.module'].search([('name', '=', 'v9c_backend_theme')]).button_immediate_uninstall()
    print 'DROP mail_ir_attachement'
    env['ir.module.module'].search([('name', '=', 'mail_ir_attachement')]).button_immediate_uninstall()
    print 'DROP account_bank_statement_import_multiline'
    env['ir.module.module'].search([('name', '=', 'account_bank_statement_import_multiline')]).button_immediate_uninstall()
    print 'DROP letsencrypt'
    env['ir.module.module'].search([('name', '=', 'letsencrypt')]).button_immediate_uninstall()
    print 'DROP auto_backup'
    env['ir.module.module'].search([('name', '=', 'auto_backup')]).button_immediate_uninstall()
    print 'DROP report_xlsx'
    env['ir.module.module'].search([('name', '=', 'report_xlsx')]).button_immediate_uninstall()
    print 'DROP attachment_preview'
    env['ir.module.module'].search([('name', '=', 'attachment_preview')]).button_immediate_uninstall()
    print 'DROP web_keyboard_navigation'
    env['ir.module.module'].search([('name', '=', 'web_keyboard_navigation')]).button_immediate_uninstall()
    print 'DROP report_xlsx'
    env['ir.module.module'].search([('name', '=', 'report_xlsx')]).button_immediate_uninstall()
    print 'DROP database_cleanup'
    env['ir.module.module'].search([('name', '=', 'database_cleanup')]).button_immediate_uninstall()
    
    print 'DROP account'
    env['ir.module.module'].search([('name', '=', 'account')]).button_immediate_uninstall()
    print 'DROP analytic'
    env['ir.module.module'].search([('name', '=', 'analytic')]).button_immediate_uninstall()
    print 'DROP board'
    env['ir.module.module'].search([('name', '=', 'board')]).button_immediate_uninstall()
    print 'DROP product'
    env['ir.module.module'].search([('name', '=', 'product')]).button_immediate_uninstall()
    print 'DROP sales_team'
    env['ir.module.module'].search([('name', '=', 'sales_team')]).button_immediate_uninstall()
    print 'DROP web_diagram'
    env['ir.module.module'].search([('name', '=', 'web_diagram')]).button_immediate_uninstall()
    print 'DROP web_list_view_sticky'
    env['ir.module.module'].search([('name', '=', 'web_list_view_sticky')]).button_immediate_uninstall()
    print 'DROP web_tip'
    env['ir.module.module'].search([('name', '=', 'web_tip')]).button_immediate_uninstall()
    print 'DROP partner_identification'
    env['ir.module.module'].search([('name', '=', 'partner_identification')]).button_immediate_uninstall()

    print 'DROP school_student_group'
    env['ir.module.module'].search([('name', '=', 'school_student_group')]).button_immediate_uninstall()
    print 'DROP school_student_group_classroom'
    env['ir.module.module'].search([('name', '=', 'school_student_group_classroom')]).button_immediate_uninstall()
    
    print 'DELETE UNUSED RECORDS'
    env['ir.filters'].search([('id','=','62')]).unlink()
    env['res.groups'].search([('category_id.id','=','23')]).unlink()

if __name__ == '__main__':
    main()