from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    principal_id = fields.One2many(
        "school.detail",
        "principal",
        string="Principal",
    )
