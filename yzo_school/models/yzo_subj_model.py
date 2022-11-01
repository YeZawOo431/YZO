from odoo import models,fields

class SubjectModel(models.Model):
    _name="yzo.subj.model"
    _description="Subjects"

    name=fields.Char("Subject Name:")
    
    

