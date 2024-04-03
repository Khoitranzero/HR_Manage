# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class Job(osv.osv):
    _name = "job"
    _columns = {
        'job_id': fields.char('ID công việc'),
        'job_title': fields.char('Chức danh công việc'),
        'description': fields.char('Mô tả công việc'),
        'employee_ids': fields.one2many('employee', 'job_id', 'Nhân viên'),
    }

    _sql_constraints = [
        ('unique_job_id', 'UNIQUE(job_id)', u'ID không phù hợp'),
        ('unique_employee_ids', 'UNIQUE(employee_ids)', u'Nhân viên không phù hợp'),
    ]
Job()