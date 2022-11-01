from odoo import fields,models,api

class SchoolMajor(models.Model):
    '''Subject Inforamtion Model'''
    _name="school.major"
    _description="Subjects"

    name=fields.Char(string="Subject")
    author=fields.Char(string="Author")
    edition=fields.Text(string="Edition")
    publisher=fields.Text(string="Publisher")

    teacher_id=fields.Many2one('school.pj','Subject Teacher')
