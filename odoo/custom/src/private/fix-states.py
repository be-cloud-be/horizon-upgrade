#!/usr/bin/env python
from __future__ import print_function
import click

import click_odoo

@click.command()
@click_odoo.env_options(default_log_level='error')
def main(env):
    
    env['school.individual_course_group'].search([('valuated_program_id','!=',False)]).state = '0_valuated'
    
    env['school.individual_course_group'].search([('valuated_program_id','=',False),('acquiered','=','A'),('final_result_bool','=',False)]).state = '0_valuated'
    
    env['school.individual_course_group'].search([('valuated_program_id','=',False),('acquiered','=','A')]).state = '6_success'
    
    env['school.individual_course_group'].search([('valuated_program_id','=',False),('acquiered','=','NA'),('final_result_bool','=',True)]).state = '7_failed'

    env['school.individual_course_group'].search([('valuated_program_id','=',False),('acquiered','=','NA'),('final_result_bool','=',False)]).state = '5_progress'
            
if __name__ == '__main__':
    main()