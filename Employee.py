# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
import datetime


class Employee(osv.osv):
    _name = "employee"
    _columns = {
        'employee_id': fields.char('Mã nhân viên'),
        'employee_name': fields.char('Tên nhân viên'),
        'employee_gender': fields.selection([('male', 'Nam'), ('female', 'Nữ'), ('other', 'Khác')], 'Giới tính'),
        'employee_address': fields.text('Địa chỉ'),
        'gmail': fields.char('Gmail'),
        'hire_date': fields.date('Ngày thuê'),
        # 'salary': fields.float('Lương'),
        # 'manage_id': fields.many2one('departments', 'ID quản lý'),
        'manage_id': fields.one2many('departments', 'manage_id', 'Nhân viên'),
        # 'job_id': fields.many2one('job','ID công việc')
    }

    _defaults = {
        'employee_id': "1232345"

    }

    def _check_gender(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            if record.employee_gender not in ['male', 'female', 'other']:
                return False
        return True

    _sql_constraints = [
        ('unique_employee_name', 'UNIQUE(employee_name)', u'tên không phù hợp')
    ]
    _constraints = [
        (_check_gender, u'hãy chon giới tính phù hợp', ['employee_gender'])
    ]


Employee()
