from odoo import api, exceptions, fields, models


class Remark(models.Model):
    _name = "remark.detail"
    _description = "remark detail"

    # line model
    rem_id = fields.Many2one("student.registration", required=True)
    remark = fields.Char("Remarks")
