from openerp import models, fields, _
from openerp import api


class HostelInformation(models.Model):
    _name = "hostel.information"

    name = fields.Char(string="Hostel Name")
    door_no = fields.Integer("Door No")
    street1 = fields.Char("Street Name")
    place_city = fields.Char("Place/City")
    district = fields.Char("District")
    state_id = fields.Many2one('res.country.state', string="State")
    country_ids = fields.Many2one('res.country', string="Country")
    availability = fields.Selection([('true', 'MEN'), ('false', 'WOMEN'), ('both', 'BOTH')], string="Available for...")
    rooms = fields.One2many("hostel.rooms", 'hostel_name', string="Rooms details")
    total_rooms = fields.Integer("Total Rooms")

    fees1_annual = fields.Integer("Single room with AC")
    fees2_annual = fields.Integer("Single room without AC")
    fees3_annual = fields.Integer("Sharing room with AC")
    fees4_annual = fields.Integer("Sharing room without AC")
    # fees1_monthly = fields.Integer("Single room with AC")
    # fees2_monthly = fields.Integer("Single room without AC")
    # fees3_monthly = fields.Integer("Sharing room with AC")
    # fees4_monthly = fields.Integer("Sharing room without AC")

    manager = fields.Char(string="Manager of the hostel")
    contact = fields.Char(string="Contact Number")

    # @api.onchange('fees1_annual')
    # def _generate_monthly_fees1(self):
    #     if self.fees1_annual:
    #         self.fees1_monthly = self.fees1_annual / 12
    #
    # @api.onchange('fees2_annual')
    # def _generate_monthly_fees2(self):
    #     if self.fees2_annual:
    #         self.fees2_monthly = self.fees2_annual / 12
    #
    # @api.onchange('fees3_annual')
    # def _generate_monthly_fees3(self):
    #     if self.fees3_annual:
    #         self.fees3_monthly = self.fees3_annual / 12
    #
    # @api.onchange('fees4_annual')
    # def _generate_monthly_fees4(self):
    #     if self.fees4_annual:
    #         self.fees4_monthly = self.fees4_annual / 12
    #
