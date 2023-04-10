from openerp import models, fields, _


class TransportApplication(models.Model):
    _name = "transport.application"
    _rec_name = 'student_name'

    student_name = fields.Many2one('school.student', string="Student Name")
    school_id = fields.Many2one("school.school", string="School name")


