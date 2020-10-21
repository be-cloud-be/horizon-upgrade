#!/usr/bin/env python
from __future__ import print_function
import click

import click_odoo

@click.command()
@click_odoo.env_options(default_log_level='error')
def main(env):
    env['ir.module.module'].search([('name', '=', 'report_xlsx')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'v9c_backend_theme')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'mail_ir_attachement')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'account_bank_statement_import_multiline')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'letsencrypt')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'auto_backup')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'report_xlsx')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'mass_editing')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'attachment_preview')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'auditlog')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'web_keyboard_navigation')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'report_xlsx')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'database_cleanup')]).button_immediate_uninstall()
    
    env['ir.module.module'].search([('name', '=', 'account')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'analytic')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'board')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'product')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'sales_team')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'web_diagram')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'web_list_view_sticky')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'web_tip')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'partner_identification')]).button_immediate_uninstall()
    
    env['ir.module.module'].search([('name', '=', 'school_student_group')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'school_student_group_classroom')]).button_immediate_uninstall()
    
    
    env['ir.filters'].search([('id','=','62')]).unlink()
    env['res.groups'].search([('category_id.id','=','23')]).unlink()

if __name__ == '__main__':
    main()