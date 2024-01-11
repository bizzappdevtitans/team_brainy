from odoo import fields, models, api, exceptions
from datetime import datetime, date
from odoo.exceptions import ValidationError


class StudentWizard(models.TransientModel):
    _name = "student.wizard"
    _description = "student wizard"

    def _get_default_student(self):
        students = self.env["student.wizard"].browse(self._context.get("active_ids"))
        return students

    student_ids = fields.Many2many(
        "student.detail", string="Student", default=_get_default_student
    )
    level = fields.Char("Level")

    def set_student_level(self):
        for record in self:
            if record.student_ids:
                for student in record.student_ids:
                    student.level = self.level
