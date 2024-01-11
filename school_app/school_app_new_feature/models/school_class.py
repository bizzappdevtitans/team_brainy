from odoo import fields, models


class SchoolClass(models.Model):
    _name = "school.class"
    _description = "Standard"

    name = fields.Char(string="Name", required=True)
    # syllabus_ids = fields.One2many('school.syllabus', 'class_id')
    division_ids = fields.One2many("school.division", "class_id")
