from odoo import fields, models


class Student(models.Model):

    _inherit = "student.detail"

    line_ids = fields.One2many(
        "result.detail",
        "result_id",
        string="Marksheet",
    )

    class_id = fields.Many2one("school.class.division", string="Class")
