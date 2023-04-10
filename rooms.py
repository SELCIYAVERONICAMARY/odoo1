from openerp import models, fields, _
from openerp import api


class HostelRooms(models.Model):
    _name = "hostel.rooms"

    name = fields.Char("Room Name")
    hostel_name = fields.Many2one('hostel.information', string="HOSTEL NAME")
    room_choice = fields.Selection(
        [('1', 'Single room with AC'), ('2', 'Single room without AC'), ('3', 'Sharing room with AC'),
         ('4', 'Sharing room without AC')],
        string="Room Available As")
    # ac_non_ac = fields.Selection([('1', 'With AC'), ('2', 'Without AC')], string="AC/Non-AC")
    status = fields.Selection([('1', 'Occupied'), ('2', 'Available')], string="Status")

    annual_room_fee = fields.Integer(compute='_compute_annual_fee', string="ANNUAL FEE")
    monthly_room_fee = fields.Integer("MONTHLY FEE")


    @api.depends('room_choice')
    def _compute_annual_fee(self):
        for record in self:
            if record.hostel_name:
                if record.room_choice == '1':
                    record.update({'annual_room_fee': self.hostel_name.fees1_annual})
                if record.room_choice == '2':
                    record.update({'annual_room_fee': self.hostel_name.fees2_annual})
                if record.room_choice == '3':
                    record.update({'annual_room_fee': self.hostel_name.fees3_annual})
                if record.room_choice == '4':
                    record.update({'annual_room_fee': self.hostel_name.fees4_annual})

    @api.onchange('annual_room_fee')
    def _generate_monthly_fees1(self):
        if self.annual_room_fee:
            self.monthly_room_fee = self.annual_room_fee / 12






    # @api.depends('hostel_name', 'room_choice')
    # def _compute_annual_fee(self):
    #     if self.hostel_name:
    #         record = self.env['hostel.information'].search([('name', '=', self.name.id)])
    #         return record
    #     if self.room_choice == '1':
    #         record1 = self.env['hostel.information'].search([('fees1_annual', '=', self.fees1.annual.id)])
    #         if len(record1) > 1:
    #             self.annual_room_fee == record1
    #



    # @api.onchange('hostel_name' 'room_choice')
    # def _generate_annual_fee1(self):
    #     if self.hostel_name:
    #         record = self.env['hostel.information'].search([('name', '=', self.id), ('fees1_annual', '=', self.id)])
    #         if self.room_choice:
    #             self.annual_room_fee = record
    #         # # self.env['hostel.information'].search(
    #         # #     [('name', '=', self.id), ('fees1_annual', '=', self.fees1_annual)])
    #         #     rec = self.env['hostel.information'].search([('fees1_annual', '=', self.fees1_annual.id)])
    #         # # recs = self.env['hostel.information'].search([('fees1_annual', '=', self.fees1_annual)])
    #         #     self.annual_room_fee = rec
