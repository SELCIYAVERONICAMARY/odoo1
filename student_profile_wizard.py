from openerp import models, fields, _


class StudentProfileWizard(models.TransientModel):
    _name = 'student.profile.wizard'
    _description = "Student List Wizard"

    student_id = fields.Many2one('school.student', string="Student name")
    student_identity = fields.Char("Student ID")
    dob = fields.Date("Date of birth")
    # department_id = fields.Many2one('school.dept', string=" School and Department")
