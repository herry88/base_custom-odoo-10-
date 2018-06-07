# -*- coding: utf-8 -*-
{
    'name': "Base Custom",

    'summary': """
        Custom odoo 10 """,

    'description': """
        additional custom modules: budgeting, project, work order, invoice, reimburse, cash advance, etc
        Juvisk Add Ons
    """,

    'author': "easierware",
    'website': "http://www.easiere.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account', 'project', 'sale', 'purchase', 'purchase_requisition','hr_maintenance'],
    # 'depends': ['base','account', 'project', 'sale', 'purchase','purchase_requisition', 'work_order'],

    # always loaded ,del company
    'data': [
        'data/sequence.xml',
        'data/reimburse_data.xml',
        'data/equipment_data.xml',
        'report/purchase_report.xml',
        'report/custom_css.xml',
        'report/account_payment_report.xml',
        'report/stock_picking_report_new.xml',
        'report/po_juvisk.xml',
        'report/customer_invoice_report.xml',
        'report/purchase_request_report.xml',
        'report/invoice_report.xml',
        'report/account_move_report.xml',
        'report/delivery_slip_report.xml',
		'report/stock_picking_report.xml',
        'report/reimburse_report.xml',
	    'report/work_order_report.xml',
        'view/invoice_view.xml',
        'view/account_view.xml',
        'view/batteryrent_view.xml',
        'view/equipment_view.xml',
        'view/area_view.xml',
        'view/project_view.xml',
        'view/reimburse_views.xml',
        'view/purchase_view.xml',
        'view/sale_view.xml'
		        
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}
