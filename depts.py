from openerp import models, fields, _
from openerp import api


class SchoolDept(models.Model):
    _name = "school.dept"

    students = fields.Integer("Total students")
    name = fields.Char(string="Dept name")

    staffs = fields.Integer("Total staffs")
    average = fields.Float(compute='_compute_avg', string='Average Of Staffs and Students')
    school_id = fields.Many2one("school.school", string="School")
    fees = fields.Integer("Fees for this department")
    pass_percentage = fields.Char("Pass Percentage")

    @api.onchange('school_id')
    def _onchange_school(self):
        if self.school_id:
            self.students = False
            self.staffs = False
            self.average = False

    @api.depends('students', 'staffs')
    def _compute_avg(self):
        if self.staffs and self.students:
            self.average = self.students + self.staffs / 2

    # @api.constrains('staffs')
    # def total_staffs(self):
    #     if self.staffs <= 0:
    #         raise ValueError('Total staffs needs to be filled')

    @api.constrains('name')
    def _validate_dept_name(self):
        if self.name:
            record = self.search([('name', '=', self.name), ('school_id', '=', self.school_id.id)])
            if len(record) > 1:
                raise UserWarning("Department name already exists in this school")

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        recs = self.search(['|', ('name', operator, name), ('school_id', operator, name)] + args, limit=limit)
        return recs.name_get()

    @api.multi
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, "%s ,%s" % (record.name, record.school_id.name)))
        return res
