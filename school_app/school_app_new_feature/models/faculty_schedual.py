from odoo import fields, models, api, exceptions


class Faculty(models.Model):

    _name = "faculty.schedual"
    _description = "Faculty schedual"

    faculty_name = fields.Char("Faculty Name")
    _rec_name = "faculty_name"
    date = fields.Date()
    department = fields.Many2one("department.detail")

    line_ids = fields.One2many(
        "time.table",
        "time_id",
        string="Time Schedual",
    )

    notes = fields.Text(string="Notes")

    def get_my_field_value(self):
        config = self.env["ir.config_parameter"]
        return config.sudo().get_param("my_module.custom_emails")

    default_email = fields.Char("Defaul Mail to", default=get_my_field_value)
