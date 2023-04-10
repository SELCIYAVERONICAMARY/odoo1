from openerp import models, fields, _
from openerp import api


class SchoolEvents(models.Model):
    _name = "school.event"

    name = fields.Char(string="Event Name")
    date = fields.Date("Date")
    time = fields.Datetime("Time")
    school_id = fields.Many2one("school.school", string="School")
    organizer = fields.Many2one("school.staff", string="Organizer")
    department_id = fields.Char("Department")
