# Copyright 2017 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Sale invoice Policy",
    "summary": """
        Sales Management: let the user choose the invoice policy on the
        order""",
    "author": "ACSONE SA/NV, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/sale-workflow",
    "category": "Sales Management",
    "version": "16.0.1.0.1",
    "license": "AGPL-3",
    "depends": ["sale_stock"],
    "data": [
        "views/product_template_view.xml",
        "views/res_config_settings_view.xml",
        "views/sale_view.xml",
    ],
    "installable": True,
    "post_init_hook": "post_init_hook",
}
