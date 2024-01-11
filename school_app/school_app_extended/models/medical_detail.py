from odoo import api, exceptions, fields, models


class Medical(models.Model):
    _name = "medical.detail"
    _description = "medical detail"

    # line model
    med_id = fields.Many2one("student.registration", required=True)
    any_disability = fields.Char("Any disability ?")
    description = fields.Text("Description")
    doc_name = fields.Char("Consultant Name")
    num = fields.Integer("Consultant's Number")
