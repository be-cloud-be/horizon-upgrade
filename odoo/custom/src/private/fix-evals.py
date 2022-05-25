#!/usr/bin/env python
from __future__ import print_function
import click

import click_odoo

@click.command()
@click_odoo.env_options(default_log_level='error')
def main(env):
    
    UPDATE school_individual_course SET final_result = first_session_result;
    UPDATE school_individual_course SET second_result = CASE WHEN second_session_result_bool THEN second_session_result ELSE NULL;
            
if __name__ == '__main__':
    main()