{
    'name': 'Fees Management',
    'version': '1.0',
    'summary': 'Fees Management',
    'description': """
    This module is used for fees management.

        """,
    "depends": ['base', 'school', 'hostelmodule','transportation'],

    'data': [
            'views/hostel_fees_view.xml',
            'views/school_fees_view.xml',
            'views/transport_fees_view.xml',



    ],
    'installable': True,
    'auto_install': False,
    'application': True,

}