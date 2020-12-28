#!/usr/bin/env python
from __future__ import print_function
import click

import click_odoo

@click.command()
@click_odoo.env_options(default_log_level='error')
def main(env):

    self.env['ir.module.module'].search([('name', '=', 'web_scheduler')]).button_immediate_uninstall()
    
    self.env['ir.module.module'].search([('name', '=', 'web_responsive')]).button_immediate_install()
            
if __name__ == '__main__':
    main()