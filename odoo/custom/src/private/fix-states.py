#!/usr/bin/env python
from __future__ import print_function
import click

import click_odoo

@click.command()
@click_odoo.env_options(default_log_level='error')
def main(env):
    for rec in env['school.individual_course_group'].search([]) :
        if rec.valuated_program_id :
            rec.state = '0_valuated'
        elif rec.acquiered == 'A' :
            rec.state = '6_success'
        elif rec.acquiered == 'NA' and rec.final_result_bool :
            rec.state = '7_failed'
        else :
            rec.state = '5_progress'
            
if __name__ == '__main__':
    main()