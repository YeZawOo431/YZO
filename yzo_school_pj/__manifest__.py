{
    'name':'My School',
    'version':'0.1',
    'author':'Ye Zaw Oo',
    'category':'School',
    'description':"""
        My School Information
    """,
    'sequence':'-100',
    'depends':[
        'base'
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/school_pj_views.xml',
        'views/section_views.xml',
        'views/question_views.xml',
        'views/major_views.xml',
        'views/exam_views.xml',
        'views/attendance_views.xml',
        'views/roll_call_views.xml'
    ]

}