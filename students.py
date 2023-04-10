from openerp import models, fields, _
from openerp import api
import json
from lxml import etree
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class SchoolStudents(models.Model):
    _name = 'school.student'
    _description = "Students Profile"

    #
    # @api.model
    # def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
    #     res = super(SchoolStudents, self).fields_view_get(view_id=view_id,
    #                                                       view_type=view_type,
    #                                                       toolbar=toolbar,
    #                                                       submenu=submenu)
    #
    #     if self.env.user.has_group('base.group_user'):
    #         doc = etree.XML(res['arch'])
    #
    #         for field in res['fields']:
    #             for node in doc.xpath("//field[@name='name']"):
    #                 node.set("readonly", "1")
    #                 modifiers = json.loads(node.get("modifiers"))
    #                 modifiers['readonly'] = True
    #                 node.set("modifiers", json.dumps(modifiers))
    #         res['arch'] = etree.tostring(doc)
    #     return res

    @api.constrains('student_id')
    def _validate_student_id(self):
        if self.student_id:
            record = self.search([('student_id', '=', self.student_id)])
            # self.env['school.school'].search()
            if len(record) > 1:
                raise UserWarning("Student ID must be unique")

    name = fields.Char("Student Name", required=True)
    student_id = fields.Char("Student ID")
    dob = fields.Date("Date of birth")
    student_image = fields.Binary("Student Image")

    print(type(dob))
    # date = fields.Date(string='Today date', default=datetime.today())
    age = fields.Char(string="Age")
    standard = fields.Selection(
        [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
         ('10', '10'), ('11', '11'), ('12', '12')], string="Class")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")
    # school_id = fields.Many2one('school.school', string="School")
    # school_code = fields.Char(string="School Code")
    department_id = fields.Many2one('school.dept', string=" School and Department")
    current_day = date.today()
    print("", current_day)
    print(type(current_day))
    hostel_dayscholar = fields.Selection([('1', 'Hostel'), ('2', 'Day scholar')], string="Hostel/Day scholar")
    transport = fields.Selection([('1', 'School Tansport'), ('2', 'Private')], string="Transportation")

    @api.onchange('dob')
    def set_age(self):
        if self.dob:
            self.age = relativedelta(datetime.today().date(), datetime.strptime(self.dob, "%Y-%m-%d")).years

    # @api.depends('dob')
    # def age_calc(self):
    #     if self.dob:
    #          self.age = (datetime.today().date() - datetime.strptime(self.dob,
    #                                                                 '%Y-%m-%d').date()).days.


    @api.onchange('school_id')
    def generate_school_code(self):
        for record in self:
            if self.school_id:
                record.update({'school_code': self.school_id.school_code})







