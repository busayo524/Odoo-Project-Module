{
    'name': 'Project Access Restriction',
    'version': '15.0.1.0.0',
    'summary': 'Restrict project visibility to assigned users only',
    'category': 'Project',
    'depends': ['project'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}