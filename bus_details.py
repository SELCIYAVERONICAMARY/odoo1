from openerp import models, fields, _


class BusDetails(models.Model):
    _name = "bus.details"
    _rec_name = 'bus_number'

    bus_number = fields.Char("Bus Number")
    bus_route = fields.Char("Bus Route")
    school_id = fields.Many2one("school.school", string="School name")
    capacity = fields.Char("Capacity")
    driver = fields.Char("Driver Name")
    contact_no = fields.Char("Contact Number")


