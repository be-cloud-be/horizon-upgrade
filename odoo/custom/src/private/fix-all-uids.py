#!/usr/bin/env python
from __future__ import print_function
import click

import click_odoo

@click.command()
@click_odoo.env_options(default_log_level='error')
def main(env):
    for rec in env['school.program'].search([]) :
        if not rec.uid:
            rec.uid = 'CYC-%05d' % rec.id
    for rec in env['school.bloc'].search([]) :
        if not rec.uid:
            rec.uid = 'BLOC-%05d' % rec.id
    for rec in env['school.course_group'].search([]) :
        if not rec.uid:
            rec.uid = 'UE-%05d' % rec.id
    for rec in env['school.course'].search([]) :
        if not rec.uid:
            rec.uid = 'AA-%05d' % rec.id
    for rec in env['school.individual_program'].search([]) :
        if not rec.uid:
            rec.uid = 'CIE-%05d' % rec.id
    for rec in env['school.individual_bloc'].search([]) :
        if not rec.uid:
            rec.uid = 'PAE-%05d' % rec.id
    for rec in env['school.individual_course_group'].search([]) :
        if not rec.uid:
            rec.uid = 'UEI-%05d' % rec.id
    for rec in env['school.individual_course'].search([]) :
        if not rec.uid:
            rec.uid = 'AAI-%05d' % rec.id
if __name__ == '__main__':
    main()