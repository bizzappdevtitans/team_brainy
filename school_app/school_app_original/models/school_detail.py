from odoo import fields, models, api, exceptions, _
from odoo.exceptions import ValidationError

try:
    from collections.abc import Callable  # noqa
except ImportError:
    from collections import Callable


class School(models.Model):
    """
    Describes a School Deails.
    """

    _name = "school.detail"
    _description = "school detail"

    name = fields.Char(string="School Name", required=True)

    # principal = fields.Char("Principal")
    principal = fields.Many2one("res.partner", string="Principal", index=True)
    teachers = fields.Many2many("teacher.detail", string="Teachers", index=True)

    address = fields.Text("Adrress")
    school_id = fields.Integer("School ID")
    school_web = fields.Char(string="School Website")

    phone_number = fields.Char(string="Phone Number")
    meadium = fields.Selection(
        [("english", "English"), ("hindi", "Hindi"), ("gujrati", "Gujrati")],
        "Meadium",
        default="english",
    )
    # school_rating = fields.Float("School Rating", (3, 2))
    sports = fields.Boolean(string="Have Sports Center?", default=True)
    image = fields.Binary("School Image")
    level = fields.Selection(
        [
            ("kg", "Kinder Garden"),
            ("primary", "Primary"),
            ("secondary", "Secondary"),
            ("higsecondary", "Higher Secondary"),
        ],
        "Level",
        default="primary",
    )
    rating = fields.Selection(
        [
            ("0", "Not Good"),
            ("1", "Average"),
            ("2", "Good"),
            ("3", "Very Good"),
            ("4", "Excellent"),
        ],
        default="0",
    )

    currency_id = fields.Many2one("res.currency")  # , string="Valuta", required=True)
    fee = fields.Monetary(string="Fee")

    @api.constrains("phone_number")
    def _constrain_phone_number_valid(self):
        for school in self:
            if school.phone_number and not school._check_phone_number():
                raise ValidationError(
                    "%s is an invalid phone_number" % school.phone_number
                )

    def _check_phone_number(self):
        # self.ensure_one()
        digits = [int(x) for x in self.phone_number if x.isdigit()]
        if len(digits) == 10:
            return digits

    @api.model
    def create(self, vals):
        vals.update({"school_id": 9})
        res = super(School, self).create(vals)
        # print("\n\n .......called.......", res, "\n\n")
        return res

    @api.model
    def name_search(self, name, args=None, operator="ilike", limit=100):
        args = args or []
        recs = self.search([("principal", operator, name)] + args, limit=limit)
        if not recs.name:
            return super(ResPartner, self).name_search(
                name=name, args=args, operator=operator, limit=limit
            )
        return recs.name_get()
