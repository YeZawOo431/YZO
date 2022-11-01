from odoo import models,fields,api

class ExamReportWizard(models.TransientModel):
    _name="exam.report.wizard"
    _description="Exam Report"

    student_id=fields.Many2one(string='Student Name',comodel_name='yzo.school.model',domain=[('role','=','student')])

    # def action_print_report(self):
    #     return


    # def get_data(self):
    #     exams=self.env['yzo.exam.line'].search[()]

    #     for rec in exams:

    #         if self.student_id:
    #             if rec.stu_id==self.student_id:
    #                 subj=rec.parent_id
    #                 score=rec.score