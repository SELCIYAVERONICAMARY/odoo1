from openerp import models, fields, _


class TransportationInformation(models.Model):
    _name = "transportation.information"

    name = fields.Char(string="Transportation Name")
    school_id = fields.Many2one('school.school', string="For School")
    total_bus = fields.Integer("Total Bus")
    bus_details = fields.One2many("bus.details", 'school_id', string="Bus Number and Route")

    # fees1_annual = fields.Integer("Single room with AC")
    # fees2_annual = fields.Integer("Single room without AC")
    # fees3_annual = fields.Integer("Sharing room with AC")
    # fees4_annual = fields.Integer("Sharing room without AC")
    # fees1_monthly = fields.Integer("Single room with AC")
    # fees2_monthly = fields.Integer("Single room without AC")
    # fees3_monthly = fields.Integer("Sharing room with AC")
    # fees4_monthly = fields.Integer("Sharing room without AC")

    manager = fields.Char(string="Manager")
    contact = fields.Char(string="Contact Number")

