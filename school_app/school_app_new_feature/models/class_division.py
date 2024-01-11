from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class SchoolClassDivision(models.Model):
    _name = "school.class.division"
    _description = "Class room"
    _inherit = ["mail.thread"]

    @api.model
    def create(self, vals):
        """Return the name as a str of class + division"""
        class_id = self.env["school.class"].browse(vals["class_id"])
        division_id = self.env["school.division"].browse(vals["division_id"])
        name = str(class_id.name + "-" + division_id.division)
        vals["name"] = name
        return super(SchoolClassDivision, self).create(vals)

    def view_students(self):  # smart button
        """Return the list of current students in this class"""
        self.ensure_one()
        students = self.env["student.detail"].search([("class_id", "=", self.id)])
        students_list = students.mapped("id")
        return {
            "domain": [("id", "in", students_list)],
            "name": _("Students"),
            "view_mode": "tree,form",
            "res_model": "student.detail",
            "view_id": False,
            "context": {"default_class_id": self.id},
            "type": "ir.actions.act_window",
        }

    def _get_student_count(self):
        """Return the number of students in the class"""
        for rec in self:
            students = self.env["student.detail"].search([("class_id", "=", rec.id)])
            student_count = len(students) if students else 0
            rec.update({"student_count": student_count})

    name = fields.Char(string="Name", readonly=True)
    actual_strength = fields.Integer(string="Class Strength")
    faculty = fields.Many2one("teacher.detail", string="Class Faculty")
    academic_year_id = fields.Many2one(
        "academic.year",
        string="Academic Year",
        required=True,
    )

    class_id = fields.Many2one("school.class", string="Class", required=True)
    division_id = fields.Many2one("school.division", string="Division", required=True)

    student_ids = fields.One2many("student.detail", "class_id", string="Students")

    student_count = fields.Integer(
        string="Students Count", compute="_get_student_count"
    )

    @api.constrains("actual_strength")
    def validate_strength(self):
        """Return Validation error if
        the students strength is not a non-zero number"""
        for rec in self:
            if rec.actual_strength <= 0:
                raise ValidationError(_("Strength must be a Non-Zero value"))
