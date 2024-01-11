from odoo import api, exceptions, fields, models


class General(models.Model):
    _name = "general.detail"
    _description = "general detail"

    # line model
    reg_id = fields.Many2one("student.registration", required=True)
    achivements = fields.Char("Achivements")
    level = fields.Char("Level")
    Win = fields.Boolean("Winner?")
