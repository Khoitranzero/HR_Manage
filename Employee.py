# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
import datetime
import string
import random
# from datetime import datetime


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
        'jobshift_ids': fields.many2one('jobshifts', 'Các ca làm'),
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

    def _check_employee_name_not_empty(self, cr, uid, ids, context=None):
        for employee in self.browse(cr, uid, ids, context=context):
            if not employee.employee_name:
                return False
        return True

    def _check_gmail_not_empty(self, cr, uid, ids, context=None):
        for employee in self.browse(cr, uid, ids, context=context):
            if not employee.gmail:
                return False
        return True
    def _check_birth_day(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            if record.birth_day:
                birth_date = datetime.datetime.strptime(record.birth_day, '%Y-%m-%d').date()
                if birth_date > datetime.date.today():
                    return False
        return True

    def _check_start_day(self, cr, uid, ids, context=None):
        for employee in self.browse(cr, uid, ids, context=context):
            if employee.birth_day > employee.start_day:
                return False
        return True
    def _check_valid_gmail(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            if record.gmail and not record.gmail.endswith('@gmail.com'):
                return False
        return True

    def _check_18age(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            if record.birth_day:
                birth_date = datetime.strptime(record.birth_day, '%Y-%m-%d').date()
                age = datetime.now().date().year - birth_date.year
                if age < 18:
                    return False
        return True

    _sql_constraints = [
        ('unique_employee_id', 'UNIQUE(employee_id)', u'ID không phù hợp'),
        ('unique_gmail', 'UNIQUE(gmail)', u'Gmail này đã tồn tại, vui lòng nhập lại gmail phù hợp'),

    ]

    _constraints = [
        (_check_gender, u'Hãy chọn giới tính phù hợp', ['employee_gender']),
        (_check_birth_day, u'Ngày sinh không phù hợp', ['birth_day']),
        (_check_start_day, u'Ngày vào làm không phù hợp', ['start_day','birth_day']),
        (_check_valid_gmail, u'Gmail không hợp lệ', ['gmail']),
        (_check_employee_name_not_empty, u'Tên nhân viên không được để trống!', ['employee_name']),
        (_check_gmail_not_empty, u'Gmail nhân viên không được để trống!', ['gmail']),
        (_check_18age, u'Nhân viên chưa đủ 18 tuổi', ['birth_day']),
    ]


Employee()