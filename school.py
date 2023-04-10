from openerp import models, fields, _
from openerp import api



class SchoolSchool(models.Model):
    _name = "school.school"

    name = fields.Char(string="School Name")
    school_code = fields.Char(string="School Code")
    tag_line = fields.Text("Tag")
    school_image = fields.Binary()
    street1 = fields.Char("Street")
    # address = fields.Char(string="Address")
    door_no = fields.Integer("Door No")
    street2 = fields.Char("Street Name")
    place_city = fields.Char("Place/City")
    district = fields.Char("District")
    state_id = fields.Many2one('res.country.state', string="State")
    country_ids = fields.Many2one('res.country', string="Country")
    achievements = fields.Text("Achievements Of School")

    # country_id = fields.Many2one('res.country', string="Country")


    # country_ids = fields.Many2many('res.country','school_country_rel','school_rel', 'country_rel', string="Country")

    department_ids = fields.One2many("school.dept", 'school_id', string="Department")
    staff_id = fields.One2many("school.staff", 'school_id', string="Staffs")
    contact = fields.Char("Administrator")



    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):

        if args is None:
            args = []
        recs = self.search(['|', ('name', operator, name), ('school_code', operator, name)] + args, limit=limit)
        return recs.name_get()

    @api.multi
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, "%s ,%s" % (record.name, record.school_code)))
        return res


    # @api.model
    # def create(self, vals):
    #     vals = {'name': 'ABC', 'tag_line': 'this school name is abc','school_code': '12345656'}
    #     res = super(SchoolSchool, self).create(vals)
    #     return res

