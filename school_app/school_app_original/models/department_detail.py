from odoo import fields, models, api, exceptions
from odoo.exceptions import ValidationError


class Department(models.Model):
    """
    Describes a Department Deails.
    """

    _name = "department.detail"
    _description = "department detail"

    name = fields.Char(string="Department Manager Name", required=True)

    dept = fields.Selection(
        [
            ("Science", "6.Science & Technology"),
            ("Maths", "5.Mathematics"),
            ("Social", "4.Social Science"),
            ("Language", "3.Language"),
            ("Practical Training", "2.Sports"),
            ("Admin", " 1.Administration"),
        ],
        string="Department",
        default="Admin",
    )
    _rec_name = "dept"
    students = fields.Integer("Total Students")

    dept_no = fields.Integer("Department Number")

    activity = fields.Text(string="Activities")
    activity_date = fields.Date("Event Date")

    # header model
    line_ids = fields.One2many(
        "department.checkout.line",
        "checkout_id",
        string="Notice",
    )

    student_count = fields.Integer(compute="compute_student")

    def compute_student(self):
        related = "act_id.student_count"
        for record in self:
            record.student_count = self.env["student.detail"].search_count(
                [("act_id", "=", self.id)]
            )

    def get_student(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "student",
            "view_mode": "tree,form",
            "res_model": "student.detail",
            "domain": [("act_id", "=", self.id)],
        }
