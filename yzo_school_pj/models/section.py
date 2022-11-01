from odoo import fields,models,api

class SectionPJ(models.Model):
    _name="section.pj"
    _description="Sections"
    _rec_name="section_name"    #to display when sections are created

    section_name=fields.Char("Section Name:")
   
    teacher_id=fields.Many2one('school.pj',string="Teacher Head:")

    section_ids=fields.One2many('section.line','section_id',string="Student Name:")

    def set_roll_no(self):      #for roll number
        roll_no=0
        for line in self.section_ids:
            roll_no+=1
            line.roll_no=roll_no
        return

    @api.model
    def create(self,vals):          #overwrite create method
        res=super(SectionPJ,self).create(vals)
        res.set_roll_no()
        return res

    def write(self,values):         #overwrite write method
        res=super(SectionPJ,self).write(values)
        self.set_roll_no()
        return res


class SectionLine(models.Model):
    _name="section.line"
    _description="Sections Line"
    _rec_name="student_id" #to display in student name of exam

    roll_no=fields.Integer("Roll No:")
    student_id=fields.Many2one('school.pj',string="Student Name:")

    section_id=fields.Many2one('section.pj')

