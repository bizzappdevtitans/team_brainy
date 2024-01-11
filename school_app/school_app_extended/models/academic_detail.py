from odoo import api, exceptions, fields, models


class Academic(models.Model):
    _name = "academic.detail"
    _description = "academic detail"

    # line model
    acm_id = fields.Many2one("student.registration", required=True)
    last_school = fields.Char("Last School")
    academic_year = fields.Date("Academic Year")
    last_std = fields.Integer("PassOut Standard ")
    living_certificate = fields.Binary("Living Cetificate")
