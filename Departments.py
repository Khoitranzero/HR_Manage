# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
import datetime

class Departments(osv.osv):
    _name = "departments"
    _columns = {
        'departments_id': fields.char('Mã phòng ban'),
        'departments_name': fields.char('Tên phòng ban'),
        'manage_id': fields.many2one('employee', 'ID quản lý'),
    }

Departments()