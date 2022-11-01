{
    'name': 'Hospital Management',
    'version': ' 1.0.0',
    'category': 'Hospital',
    'summary': 'Hospital management system',
    'description': """Hospital management system""",
    'depends': [
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
    ],
    'demo': [

    ],
    'sequence': '-100',
    'application': True,
    'installable': True,
    'auto-install': False,
    'License': 'LGPL-3'



}
