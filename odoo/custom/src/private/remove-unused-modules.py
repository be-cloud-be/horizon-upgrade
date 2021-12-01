#!/usr/bin/env python
from __future__ import print_function
import click

import click_odoo

@click.command()
@click_odoo.env_options(default_log_level='error')
def main(env):
    env['ir.module.module'].search([('name', '=', 'v9c_backend_theme'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'mail_ir_attachement'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'account_bank_statement_import_multiline'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'letsencrypt'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'auto_backup'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'report_xlsx'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'attachment_preview'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'web_keyboard_navigation'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'report_xlsx'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'database_cleanup'),("state",'=','installed')]).button_immediate_uninstall()
    
    env['ir.module.module'].search([('name', '=', 'account'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'analytic'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'board'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'product'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'sales_team'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'web_diagram'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'web_list_view_sticky'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'web_tip'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'partner_identification'),("state",'=','installed')]).button_immediate_uninstall()

    env['ir.module.module'].search([('name', '=', 'school_student_group'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'school_student_group_classroom'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'school_split_cg_tool'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'school_documentation'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'school_diploma'),("state",'=','installed')]).button_immediate_uninstall()
    env['ir.module.module'].search([('name', '=', 'school_covid_followup'),("state",'=','installed')]).button_immediate_uninstall()
    
    env['ir.filters'].search([('id','=','62')]).unlink()
    env['res.groups'].search([('category_id.id','=','23')]).unlink()

if __name__ == '__main__':
    main()