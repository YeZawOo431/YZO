from odoo import models,fields,api

class YZO_School(models.Model):
    _name="yzo.school.model"
    _description="School Information"

    avatar=fields.Binary("Photo")
    roll_no=fields.Char("Roll Number:")
    name=fields.Char("Name:",required=True)
    father_name=fields.Char("Father Name:")
    date_of_birth=fields.Date(string="Date Of Birth:")
    phone_no=fields.Char("Phone Number:")
    address=fields.Text(string="Address:")


    role=fields.Selection(
         [('student','Student'),('teacher','Teacher')],'Role:'
    )
    
    state = fields.Selection(selection=[
        ('old', 'Old'),
        ('new', 'New'),
        ('current', 'Current')], string='State:', copy=False,tracking=True, default="current"
    ) # required=True (Invalid Field Error)

    def action_summary(self):
        return