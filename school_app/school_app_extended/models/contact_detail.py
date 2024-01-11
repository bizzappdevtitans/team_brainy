from odoo import api, exceptions, fields, models
from odoo.exceptions import ValidationError


class Contact(models.Model):
    _name = "contact.detail"
    _description = "contact detail"
    _inherits = {"res.partner": "partner_id"}

    # line model
    con_id = fields.Many2one("student.registration", required=True)
    contact_number = fields.Char("Emergency number")
    relation = fields.Char("Relationship")
    guardian_name = fields.Many2one(
        "res.partner",
        string="Guardian",
    )

    @api.constrains("contact_number")
    def _constrain_contact_number_valid(self):
        for number in self:
            if number.contact_number and not number._check_contact_number():
                raise ValidationError(
                    "%s is an invalid phone_number" % number.contact_number
                )

    def _check_contact_number(self):
        self.ensure_one()
        digits = [int(x) for x in self.contact_number if x.isdigit()]
        if len(digits) == 10:
            return digits
