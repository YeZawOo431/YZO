from odoo import models,fields,api

class SchoolPJ(models.Model):
    _name="school.pj"
    _description="School Information"

    avatar=fields.Binary("Profile Photo:")
    # roll_no=fields.Char("Roll Number:")
    name=fields.Char("Name:",required=True)
    father_name=fields.Char("Father Name:")
    gender=fields.Selection([
     ('male','Male'),
     ('female','Female')], string="Gender")
    date_of_birth=fields.Date(string="Date Of Birth:")
    phone_no=fields.Char("Phone Number:")
    address=fields.Text(string="Address:")


    role=fields.Selection(
         [('student','Student'),('teacher','Teacher')],string='Role:',default='student'
    )

    teacher_role=fields.Selection([
        ('principal','Principal'),
        ('teacher','Teacher'),
        ('head','Teacher Head')],string='Teacher Role:'
    )

