# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
import datetime

class Departments(osv.osv):
    _name = "departments"
    _columns = {
        'departments_id': fields.char('Mã phòng ban'),
        'departments_name': fields.char('Tên phòng ban'),
        'manager_id': fields.many2one('employee', 'Quản lý', required=True),
        'employee_ids': fields.one2many('employee', 'department_id', 'Nhân viên'),
        'employee_count': fields.integer('Số lượng nhân viên', compute='_compute_employee_count', store=True),
        'max_employee_count': fields.integer('Số lượng nhân viên tối đa', help="Số lượng nhân viên tối đa cho phòng ban này"),
    }

    _sql_constraints = [
        ('unique_manager_id', 'unique(manager_id)', u'Quản lý phòng ban phải duy nhất!'),
        ('unique_departments_id', 'unique(departments_id)', u'ID phòng ban phải duy nhất!'),
    ]

    def _compute_employee_count(self, cr, uid, ids, field_name, arg, context=None):
        for department in self.browse(cr, uid, ids, context=context):
            count = 0
            if department.employee_ids:
                count = len(department.employee_ids)
            department.employee_count = count

    # _defaults = {
    #     'employee_count': _compute_employee_count
    # }

    def _check_max_employee_count(self, cr, uid, ids, context=None):
        for department in self.browse(cr, uid, ids, context=context):
            if department.max_employee_count and department.employee_count >= department.max_employee_count:
                return False
        return True

    def _check_departments_name_not_empty(self, cr, uid, ids, context=None):
        for department in self.browse(cr, uid, ids, context=context):
            if not department.departments_name:
                return False
        return True

    def _check_departments_id_not_empty(self, cr, uid, ids, context=None):
        for department in self.browse(cr, uid, ids, context=context):
            if not department.departments_id:
                return False
        return True
    _constraints = [
        (_check_max_employee_count, u'Phòng ban đã đủ nhân viên. Không thể thêm nhân viên mới!', []),
        (_check_departments_name_not_empty, u'Tên phòng ban không được để trống!', ['departments_name']),
        (_check_departments_id_not_empty, u'ID phòng ban không được để trống!', ['departments_id']),
    ]


Departments()
