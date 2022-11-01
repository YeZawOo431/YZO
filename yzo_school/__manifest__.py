{
    'name':'My Private School',
    'version':'0.1',
    'author':'Ye Zaw Oo',
    'category':'School',
    'description':"""
        My School Information
    """,
    'sequence':'1',
    'depends':[
        'base'
    ],
    'data':[
        'security/ir.model.access.csv',
        'report/exam_reports.xml',
        'wizard/exam_report_views.xml',
        'views/school_views.xml',
        'views/subject_views.xml',
        'views/exam_views.xml',
        
    ]

}