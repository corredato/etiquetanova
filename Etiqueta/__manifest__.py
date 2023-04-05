# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Etiqueta',
    'version' : '1.0',
    'summary': 'Imprimir Etiqueta Zebra',
    'sequence': -100,
    'description': """Imprimir Etiqueta Zebra""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com/page/billing',
    'depends': ['sale'],
    'data': ['security/ir.model.access.csv',
             'views/etiqueta.xml',
             'views/sale.xml',
             'report/report.xml',
             'report/etiqueta.xml',],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
