from openerp import models, fields, _
from openerp import api

class SchoolFees(models.Model):
    _name = "school.fees"
    _rec_name = 'student_id'

    student_id = fields.Many2one("school.admission", string="Student name")
    payment_type = fields.Selection([('cash', 'Cash'), ('upi', 'UPI'), ('netbanking', 'Net Banking'), ('creditcard','Credit card')], string="Mode of payment")
    # payment_method = fields.Selection([('monthly', 'Monthly'), ('annual', 'Annual')], string="Payment Method annual/monthly?")
    amount = fields.Integer(string="Fees Amount")

    @api.onchange('student_id')
    def _generate_fees(self):
        for rec in self:
            if rec.student_id:
                rec.update({'amount': self.student_id.department_id.fees})




    




