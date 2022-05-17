#!/usr/bin/env python
from __future__ import print_function
import click

import click_odoo

@click.command()
@click_odoo.env_options(default_log_level='error')
def main(env):
    
    \c odoo_v9
    
    COPY (select id, teacher_id from school_course_group) TO '/tmp/teachers.csv';
    
    \c odoo_v14
    
    create table teacher_import (id integer, teacher_id integer);
    
    COPY teacher_import FROM '/tmp/teachers.csv';
    
    UPDATE school_course_group set responsible_id = teacher_import.teacher_id FROM teacher_import WHERE school_course_group.id = teacher_import.id; 
            
    DROP TABLE teacher_import;
            
if __name__ == '__main__':
    main()