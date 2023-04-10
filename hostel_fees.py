from openerp import models, fields, _
from openerp import api

class HostelFees(models.Model):
    _name = "hostel.fees"

    name = fields.Many2one("hostel.application", string="Student name")
    payment_type = fields.Selection([('cash', 'Cash'), ('upi', 'UPI'), ('netbanking', 'Net Banking'), ('creditcard','Credit card')], string="Mode of payment")
    payment_method = fields.Selection([('monthly', 'Monthly'), ('annual', 'Annual')], string="Payment Method annual/monthly?")
    amount1 = fields.Integer(compute="_generate_amount", string="Monthly fees")
    amount2 = fields.Integer(compute="_generate_amount", string="Annual fees")



    # def _action_annual_fee(self):
    #     if self.payment_method == 'monthly':




    @api.depends('payment_method')
    def _generate_amount(self):
        for record in self:
            if record.name:
                if record.payment_method == 'monthly':
                    record.update({'amount1': self.name.room_selection.monthly_room_fee})
                if record.payment_method == 'annual':
                    record.update({'amount2': self.name.room_selection.annual_room_fee})
