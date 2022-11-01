from odoo import models,fields,api
from datetime import date

class HospitalPatient(models.Model):
    _name="hospital.patient"
    _inherit=["mail.thread","mail.activity.mixin"]
    _description="Hospital Patient"


    name=fields.Char(string="Name",tracking=True)
    date_of_birth=fields.Date(string="Date of Birth")
    age=fields.Integer("Age",compute="_compute_age",tracking=True)
    ref=fields.Char(string="Reference")
    gender=fields.Selection([('male','Male'),('female','Female')],string="Gender",tracking=True)
    active=fields.Boolean(string="Active",default=True)
    appointment_id=fields.Many2one('hospital.appointment',string="Appointments")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            # print("REC=",rec)
            today=date.today()
            if rec.date_of_birth:
                # print(rec.date_of_birth)
                rec.age=today.year-rec.date_of_birth.year
                # print(rec.age)
            else:
                rec.age=0

