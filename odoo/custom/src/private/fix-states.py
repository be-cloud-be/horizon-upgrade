#!/usr/bin/env python
from __future__ import print_function
import click

import click_odoo

@click.command()
@click_odoo.env_options(default_log_level='error')
def main(env):
    
    env['school.individual_course_group'].search([('valuated_program_id','!=',False)]).write({'state':'0_valuated'})
    
    env['school.individual_course_group'].search([('valuated_program_id','=',False),('acquiered','=','A'),('final_result_bool','=',False)]).write({'state':'0_valuated'})
    
    env['school.individual_course_group'].search([('valuated_program_id','=',False),('acquiered','=','A')]).write({'state':'6_success'})
    
    env['school.individual_course_group'].search([('valuated_program_id','=',False),('acquiered','=','NA'),('final_result_bool','=',True)]).write({'state':'7_failed'})

    env['school.individual_course_group'].search([('valuated_program_id','=',False),('acquiered','=','NA'),('final_result_bool','=',False)]).write({'state':'5_progress'})
            
    env.cr.commit()
            
if __name__ == '__main__':
    main()