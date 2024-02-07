{
    'name': "Dokumentai",        #modulio pavadinimas
    'description': """Dokumentų valdymo programa""",
    'author': "Aurelija",
    'version': '0.0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/dokumentai_view.xml',
        'views/menu.xml',
    ],

    'application': True, # kad rodytų apps sąraše
    'installable': True,
}