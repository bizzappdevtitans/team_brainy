from odoo import fields, models


class Teacher(models.Model):

    _inherit = "teacher.detail"

    is_manager = fields.Boolean("Is manager?")
