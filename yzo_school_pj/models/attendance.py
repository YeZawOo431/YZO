from datetime import date, datetime,timedelta
from odoo import fields,models,api

class SchoolAttendance(models.Model):
    _name = "school.attendance"
    _description = "School Attendance"
    _rec_name="monthly"

    section_name = fields.Many2one('section.pj', string="Section Name:")
  
    monthly=fields.Selection([
        ('January','January'),
        ('February','February'),
        ('March','March'),
        ('April','April'),
        ('May','May'),
        ('June','June'),
        ('July','July'),
        ('August','August'),
        ('September','September'),
        ('October','October'),
        ('November','November'),
        ('December','December')],string="Month",required=True,store=True)


    attendance_line_ids = fields.One2many("school.attendance.line","attendance_line_id",string="Attendance Report")

    # @api.onchange('section_name')
    # def onchange_section_name(self):
    #     self.attendance_line_ids=[(5,0,0)]
    #     global total_point
    #     total_point={}
    #     roll_num = self.env['rollcall.line'].search([])
    #     student_ids = self.env['school.pj'].search([('role','=','student')])
    #     print(".....",roll_num)
    #     print("....",student_ids)

    #     for student in student_ids:
    #         print("student Id", student.id)
    #         print("......",roll_num.filtered(lambda x:int(x.student_id) == student.id).mapped("state"))
    #         tot_point=sum(roll_num.filtered(lambda x:int(x.student_id) == student.id).mapped("state"))
    #         # total_mark = sum(roll_num.filtered(lambda x:x.student_id == student.id))
    #         print("total state", total_point)
    #         total_point.update({student.id,tot_point})

    def check_percent(self,parm_per):
        per=""
        if parm_per < 0.06:
            per="Rejected"
        else:
            per="Accessed"
        return per

    def cal_percent(self,param_point):
        # print(param_point)
        percent=0.0
        if self.monthly in ['April','June','September','November']:
            percent=param_point/30
        elif self.monthly=='February':
            percent=param_point/28
        else:
            percent=param_point/31

        return percent

    @api.onchange('section_name','monthly')
    def onchange_sec_name(self):
        if self.section_name and self.monthly:
            self.attendance_line_ids=[(5,0,0)]
            total_point={}
            roll_num = self.env['rollcall.line'].search([])
            student_ids = self.env['school.pj'].search([('role','=','student')])

            # for line in roll_num:
            #     print("Month.....",self.monthly,line.roll_call_id.date.strftime("%B"),
            #     type(datetime.strptime(str(line.roll_call_id.date),"%Y-%m-%d").month))

            if student_ids:
                for student in student_ids:
                    
                    report_obj=roll_num.filtered(lambda x:int(x.student_id) == student.id and x.roll_call_id.date.strftime("%B") == self.monthly)
                    print("Save....",report_obj)

                    tot_point=sum(roll_num.filtered(lambda x:int(x.student_id) == student.id and x.roll_call_id.date.strftime("%B") == self.monthly).mapped("state"))

                    # print("total state", total_point)
                    total_point.update({student.id:tot_point})
                    print(total_point)



            sections = self.env['section.line'].search([])
            if sections:
                for sec in sections:
                    
                    
                    if self.section_name.section_name == sec.section_id.section_name:
                        t_point=total_point.get(int(sec.student_id))
                        percent=self.cal_percent(t_point)
                        # print("......",sec.student_id)
                        # print(total_point.get(int(sec.student_id)))
                        vals = {
                            'roll_no':sec.roll_no,
                            # 'student_id':int(sec.student_id),
                            'student_name':sec.student_id.name,
                            'total_attendances':t_point,
                            'rollcall_percent': percent,
                            'for_exam':self.check_percent(percent)
                        }
                        # self.update({'attendance_line_ids':[(0,0,vals)]})
                        self.attendance_line_ids=[(0,0,vals)]

    # @api.onchange('section_name')
    # def _onchange_percent(self):
    #     if self.section_name:
    #         name = self.section_name.attendance_line_ids.student_name
    #         self.full_day = self.env['rollcall.line'].search_count(['&', ('student_name', '=', name), ('state', '=', 1.0)])
    #         self.half_day = self.env['rollcall.line'].search_count(['&',('student_name', '=', name),('state', '=', 0.5)])
            # self.leave = self.env['leave.students'].search_count([('student_id', '=', name)])
    
    # @api.onchange('section_name')
    # def onchange_section_name(self):
    #     self.attendance_line_ids=[(5,0,0)]
    #     roll_num = self.env['school.section.line'].search([])
    #     if roll_num:
    #         for roll in roll_num:
    #             if self.section_name.name == roll.section_id.name:
    #                 vals = {
    #                     'roll_no':roll.roll_no,
    #                     'student_name':roll.student_name.name
    #                 }
    #                 self.update({'attendance_line_ids':[(0,0,vals)]})

   

class SchoolAttendanceLine(models.Model):
    _name = "school.attendance.line"
    _description = "School Attendance Line"
    _rec_name="student_name"

    roll_no = fields.Char("Roll Number")
    student_name = fields.Char("Student Name")
    total_attendances = fields.Float("Total Attendance")
    rollcall_percent = fields.Float("RollCall %")
    for_exam=fields.Char("Permission")
    
    attendance_line_id = fields.Many2one("school.attendance",string="Attendance Line ID")


    # def _total_present(self):
    #     # self.attendance_line_id=[(5,0,0)]
    #     half = self.env['roll_call_id'].search_count([('school.project.name', '=', 'school.attendance.line.student_name'),'&',('rollcall.line.state','=','0.5')])
    #     count = 0
    #     for rec in half:
    #            rec.count +=count

 
    
                
    
    