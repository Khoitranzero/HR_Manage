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
        ('unique_manager_id', 'unique(manager_id)', u'Quản lý phòng ban phải duy nhất!')
    ]

    def _compute_employee_count(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for department in self.browse(cr, uid, ids, context=context):
            res[department.id] = len(department.employee_ids)
        return res

    def _check_max_employee_count(self, cr, uid, ids, context=None):
        for department in self.browse(cr, uid, ids, context=context):
            if department.max_employee_count and department.employee_count >= department.max_employee_count:
                return False
        return True

    _constraints = [
        (_check_max_employee_count, u'Phòng ban đã đủ nhân viên. Không thể thêm nhân viên mới!', []),
    ]


Departments()
