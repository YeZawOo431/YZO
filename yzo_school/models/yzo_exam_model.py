from odoo import models,fields,api

class ExamModel(models.Model):
    _name="yzo.exam.model"
    _description="Exam Marks"
    _rec_name="subj_id"

    subj_id=fields.Many2one('yzo.subj.model',string="Subject Name: ",required=True)

    teacher_id=fields.Many2one('yzo.school.model',string="Teacher: ",required=True)

    
    child_ids=fields.One2many('yzo.exam.line','parent_id')
    
    role=fields.Selection(
         [('student','Student'),('teacher','Teacher')],'Role:'
    )
    
    state = fields.Selection(selection=[
        ('old', 'Old'),
        ('new', 'New'),
        ('current', 'Current')], string='State:', copy=False,tracking=True, default="current"
    ) # required=True (Invalid Field Error)



    class YZO_Exam(models.Model):
        _name="yzo.exam.line"
        _description="Exam Line"


        stu_id=fields.Many2one('yzo.school.model',string="Student Name:")

        parent_id=fields.Many2one('yzo.exam.model',string="")

        score=fields.Integer("Score:")

        status= fields.Char(string ='Status:',readonly=True)
                
        @api.onchange('score')
        def Onchange_score(self):

            if self.score >= 80 and self.score <= 100:
                self.status= 'Passed Distination'
            elif self.score >= 40 and self.score < 80:
                self.status='Passed'
            elif self.score < 40 and self.score >= 0:
                self.status='Failed'
            else:
                self.status='Wrong score!!!'

        


