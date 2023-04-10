from openerp import models, fields, _

class TransportFees(models.Model):
    _name = "transport.fees"

    name = fields.Char(string="Student name")
    payment_type = fields.Selection([('cash', 'Cash'), ('upi', 'UPI'), ('netbanking', 'Net Banking'), ('creditcard','Credit card')], string="Mode of payment")
    payment_method = fields.Selection([('monthly', 'Monthly'), ('annual', 'Annual')], string="Payment Method annual/monthly?")
    amount1 = fields.Integer(string="Monthly fees")
    amount2 = fields.Integer(string="Annual fees")

