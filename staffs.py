from openerp import models, fields, _
from openerp import api


class SchoolStaff(models.Model):
    _name = "school.staff"

    name = fields.Char(string="Staff name", required=True)
    mail = fields.Char(string="Email Id", required=True)
    number = fields.Char("Phone Number", required=True)
    staff_id = fields.Char("Staff ID", required=True)
    address = fields.Char(string="Address")
    door_no = fields.Integer("Door No")
    street2 = fields.Char("Street2")
    place_city = fields.Char("Place/City")
    district = fields.Char("District")
    state_id = fields.Many2one('res.country.state', string="State")
    country_ids = fields.Many2many('res.country', string="Country")
    image = fields.Binary("Staff Image")
    age = fields.Integer("Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    school_id = fields.Many2one("school.school", string="School")
    experience = fields.Integer("Experience in years")
    department_id = fields.Many2one("school.dept", string="Department")








