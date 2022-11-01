from odoo import models,fields,api

class HospitalAppointment(models.Model):
    _name="hospital.appointment"
    _inherit=["mail.thread","mail.activity.mixin"]
    _description="Hospital Appointment"
    _rec_name="patient_id"

    patient_id=fields.Many2one('hospital.patient',string="Patient")
    gender=fields.Selection(string="Gender",related='patient_id.gender')
    appointment_time=fields.Datetime(string='Appointment Time',default=fields.Datetime.now)
    booking_date=fields.Date(string="Booking Date",default=fields.Date.context_today)
    ref=fields.Char(string="Reference",help="Reference of the patient from patient records")
    prescription=fields.Html(string="Prescription")
    priority=fields.Selection([
        ('0','Normal'),
        ('1','Low'),
        ('2','High'),
        ('3','Very High')],string="Priority")
    state=fields.Selection([
        ('draft','Draft'),
        ('in_consultation','In Consultation'),
        ('done','Done'),
        ('cancel','Cancelled')],default='draft',string="Status")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref=self.patient_id.ref

    def action_test(self):
        return{
            'effect':{
                'fadeout':'slow',
                'message':'Click Successful',
                'type':'rainbow_man'
            }
        }