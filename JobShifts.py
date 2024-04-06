# -*- coding: utf-8 -*-
from openerp.osv import osv, fields


class JobShifts(osv.osv):
    _name = 'jobshifts'
    _columns = {
        'employee_id': fields.one2many('employee','jobshift_ids', 'ID nhân viên'),
        'job_shift_id': fields.char('Ca làm'),
        'start_hours': fields.datetime('Giờ bắt đầu'),
        'end_hours': fields.datetime('Giờ kết thúc'),
    }

    def _check_start_and_end_hours(self, cr, uid, ids, context=None):
        for jobshifts in self.browse(cr, uid, ids, context=context):
            if jobshifts.start_hours > jobshifts.end_hours:
                return False
        return True

    def _check_job_shift_id_not_empty(self, cr, uid, ids, context=None):
        for jobshifts in self.browse(cr, uid, ids, context=context):
            if not jobshifts.job_shift_id:
                return False
        return True
    _sql_constraints = [
        ('unique_employee_id', 'UNIQUE(employee_id)', u'ID không phù hợp'),
        ('unique_job_shift_id', 'UNIQUE(job_shift_id)', u'ID ca làm không phù hợp')
    ]

    _constraints = [
        (_check_start_and_end_hours, u'Giờ làm không phù hợp', ['start_hours','end_hours']),
        (_check_job_shift_id_not_empty, u'ID ca làm không được để trống!', ['job_shift_id']),
    ]

JobShifts()

