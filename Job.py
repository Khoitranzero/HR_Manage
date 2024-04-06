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

    def _check_job_id_not_empty(self, cr, uid, ids, context=None):
        for job in self.browse(cr, uid, ids, context=context):
            if not job.job_id:
                return False
        return True

    def _check_job_title_not_empty(self, cr, uid, ids, context=None):
        for job in self.browse(cr, uid, ids, context=context):
            if not job.job_title:
                return False
        return True
    _constraints = [
        (_check_job_title_not_empty, u'Tên công việc được để trống!', ['job_title']),
        (_check_job_id_not_empty, u'ID công việc không được để trống!', ['job_id']),
    ]
    _sql_constraints = [
        ('unique_job_id', 'UNIQUE(job_id)', u'ID không phù hợp'),
        # ('unique_employee_ids', 'UNIQUE(employee_ids)', u'Nhân viên không phù hợp'),
    ]
Job()