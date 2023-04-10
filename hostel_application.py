from openerp import models, fields, _, api
from datetime import date, datetime
from odoo.exceptions import ValidationError



class HostelApplication(models.Model):
    _name = "hostel.application"

    hostel_name = fields.Many2one("hostel.information", string="Name of the Hostel applying for")
    new_or_old = fields.Selection([('new', 'New Applicant'), ('old', 'Already a student')], string="Select Anyone")

    name = fields.Many2one("school.student", string="Name of the student")
    application_date = fields.Date("Applied on", default=datetime.today())
    state = fields.Selection([('draft','Draft'), ('waiting_for_approval', 'Waiting for Approval'), ('approved', 'Approved')], string="Status", default="draft")

    # school_name = fields.Many2one("school.student", string="School Name")
    # department = fields.Many2one("school.dept", string="Department")
    # standard = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
    #                              ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], string="Class")
    guardian_name = fields.Char("Father/Mother Name")
    contact = fields.Char("Contact Number")


    # food = fields.Selection([('needed', 'Needed'), ('not needed', 'Not Needed')], string="Food Needed/Not")
    room_selection = fields.Many2one("hostel.rooms", string="Rooms details")


    def waiting_for_approval_state(self):
        self.state = 'waiting_for_approval'

    def approval_state(self):
        self.state = 'approved'

    @api.multi
    def unlink(self):
        for record in self:
            if record.state == "draft":
                res = super(HostelApplication, self).unlink()
                return res
            else:
                raise ValidationError(_('You can only delete records which are in draft state!'))









