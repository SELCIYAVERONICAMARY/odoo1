from openerp import models, fields, _
from openerp import api
from datetime import date, datetime


class AdmissionForm(models.Model):
    _name = 'school.admission'

    name = fields.Char("Student Name", required=True)
    image = fields.Binary("Student Image")
    dob = fields.Date("Date of birth")
    age = fields.Char(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")

    street1 = fields.Char("Street")
    # address = fields.Char(string="Address")
    door_no = fields.Integer("Door No")
    street2 = fields.Char("Street Name")
    place_city = fields.Char("Place/City")
    district = fields.Char("District")
    state_id = fields.Many2one('res.country.state', string="State")
    country_ids = fields.Many2many('res.country', string="Country")
    father_name = fields.Char("Father's Name")
    father_work = fields.Char("Occupation")
    number1 = fields.Char("Contact Number")
    mother_name = fields.Char("Mother's Name")
    mother_work = fields.Char("Occupation")
    number2 = fields.Char("Contact Number")
    department_id = fields.Many2one("school.dept", string="Choose Department")
    fees_amount = fields.Integer(compute='_compute_fees', string="Fees amount")
    standard_selection = fields.Selection(
        [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
         ('10', '10'), ('11', '11'), ('12', '12')], string="Applying For Which Standard?")
    medium = fields.Selection([('english', 'English'), ('tamil', 'Tamil')])
    # previously studied school details
    school_name = fields.Char("School Name")
    standard = fields.Selection(
        [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
         ('10', '10'), ('11', '11'), ('12', '12')], string="Studied Till")
    previous_medium = fields.Selection([('english', 'English'), ('tamil', 'Tamil')])

    # hostel and transportation details
    hostel = fields.Boolean("Hostel Needed or Not?")
    hostel_application = fields.One2many('hostel.application', 'hostel_name', " Hostel Application Form")
    transportation = fields.Boolean("Transportation Needed Or Not?")
    # transport_application = fields.One2many('transport.application', 'student_name', string="Application Form")
    sibling = fields.Boolean("DO YOU HAVE ANYONE(SIBLINGS/COUSINS) WHO IS ALREADY STUDYING IN THIS SCHOOL?")
    sibling_name = fields.Char("Name of Your Sibling/Cousin")
    sibling_standard = fields.Selection(
        [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
         ('10', '10'), ('11', '11'), ('12', '12')], string="Standard")
    relationship = fields.Char("Your Relationship with them")
    applied_date = fields.Date(string='Applied on', default=datetime.today())
    school_names = fields.Many2one("school.school", string="School Names")
    codes = fields.Many2one("school.school", string="School Codes")

    @api.depends('school_names', 'department_id')
    def _compute_fees(self):
        for rec in self:
            if rec.school_names:
                if rec.department_id:
                    rec.update({'fees_amount': self.department_id.fees})

    @api.multi
    def generate_hostel_application_form(self):
        view_id = self.env.ref('hostelmodule.application_form_view').id
        context = self._context.copy()
        return {
            'name': 'application.form',
            'view_type': 'form',
            'view_mode': 'tree',
            'views': [(view_id, 'form')],
            'res_model': 'hostel.application',
            'view_id': True,
            'type': 'ir.actions.act_window',
            'res_id': self.id,
            # 'target': 'new',
            'context': context,
        }




    class InheritHostelApplication(models.Model):
        _inherit = 'hostel.application'

        field1 = fields.Char("Name of the student")





