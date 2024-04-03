# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
import datetime
import string
import random


class Employee(osv.osv):
    _name = "employee"
    _description = "Employee Information"

    def _default_employee_id(self, cr, uid, context=None):
        date_today = datetime.datetime.now().strftime('%y%m%d%M')
        return "DH" + date_today

    _columns = {
        'employee_id': fields.char('Mã nhân viên', readonly=True),
        'employee_name': fields.char('Tên nhân viên'),
        'employee_gender': fields.selection([('male', 'Nam'), ('female', 'Nữ'), ('other', 'Khác')], 'Giới tính', default='male'),
        'employee_address': fields.text('Địa chỉ'),
        'gmail': fields.char('Gmail'),
        'birth_day': fields.date('Ngày sinh'),
        'department_id': fields.many2one('departments', 'Phòng ban'),
        'job_id': fields.many2one('job', 'Công việc'),
        'start_day': fields.date('Ngày vào làm'),
        'salary': fields.float('Lương'),
    }

    _defaults = {
        'employee_id': _default_employee_id,
        'employee_gender': 'male',
    }

    def _check_gender(self, cr, uid, ids, context=None):
        for employee in self.browse(cr, uid, ids, context=context):
            if employee.employee_gender not in ['male', 'female', 'other']:
                return False
        return True

    def _check_birth_day(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            if record.birth_day:
                birth_date = datetime.datetime.strptime(record.birth_day, '%Y-%m-%d').date()
                if birth_date > datetime.date.today():
                    return False
        return True

    def _check_valid_gmail(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            if record.gmail and not record.gmail.endswith('@gmail.com'):
                return False
        return True

    _sql_constraints = [
        ('unique_employee_id', 'UNIQUE(employee_id)', u'ID không phù hợp')
    ]

    _constraints = [
        (_check_gender, u'Hãy chọn giới tính phù hợp', ['employee_gender']),
        (_check_birth_day, u'Ngày sinh không phù hợp', ['birth_day']),
        (_check_valid_gmail, u'Gmail không hợp lệ', ['gmail']),
    ]


Employee()