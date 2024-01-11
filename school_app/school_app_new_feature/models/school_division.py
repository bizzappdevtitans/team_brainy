from odoo import fields, models


class SchoolDivision(models.Model):
    _name = "school.division"
    _description = "Standard Division"

    # name = fields.Char(string="Name", required=True)
    # strength = fields.Integer(string="Class Strength")
    # faculty = fields.Many2one("teacher.detail", string="Class Faculty")
    class_id = fields.Many2one("school.class", string="Class")
    division = fields.Selection(
        [
            ("a", "A"),
            ("b", "B"),
        ],
        "Division",
        default="a",
    )
    _rec_name = "division"
