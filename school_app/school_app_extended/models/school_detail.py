from odoo import fields, models, _


class School(models.Model):
    _inherit = "school.detail"

    name = fields.Char("Name")
    reg_id = fields.Integer(compute="student_registration_form")

    def student_registration_form(self):
        reg_id = self.reg_id
        view_ref = self.env["student.registration"]
        view_id = view_ref[1] if view_ref else False

        self.ensure_one()
        res = {
            "type": "ir.actions.act_window",
            "name": _("registration"),
            "res_model": "student.registration",
            "view_type": "form",
            "view_mode": "form",
            "view_id": view_id,
            "target": "current",
            "context": {"default_partner_id": reg_id},
        }

        return res
