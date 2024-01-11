from odoo import fields, models, api, exceptions
from odoo.exceptions import ValidationError

try:
    from collections.abc import Callable
except ImportError:
    from collections import Callable


class Teacher(models.Model):
    """
    Describes a teacher Deails.
    """

    _name = "teacher.detail"
    _description = "teacher detail"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char("First Name", required=True)
    short_name = fields.Char(string="Short Name")
    email = fields.Char("Email ID")
    color = fields.Integer("color")

    sub = fields.Selection(
        [
            ("sci", "Science & Technology"),
            ("maths", "Mathematics"),
            ("social", "Social Science"),
            ("eng", "English"),
            ("hindi", "Hindi"),
            ("guj", "Gujrati"),
            ("pic", "Drawing"),
            ("pt", "Practical Training"),
            ("admin", "Administration"),
        ],
        string="Subject",
        default="",
    )
    _sql_constraints = [
        ("unique_email", "UNIQUE(email)", "Email address already exists!")
    ]

    def unlink(self):
        for name in self:
            if name:
                raise UserError(_("You cannot Delete this record"))
        return super(Teacher, self).unlink()

    @api.model
    def name_get(self):
        res = []
        for field in self:
            # name = field.name
            if field.short_name:
                res.append((field.id, "%s : %s" % (field.short_name, field.name)))
        return res
