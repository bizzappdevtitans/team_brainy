from odoo import fields, models


class CheckoutStage(models.Model):
    _name = "school.addmission.stage"
    _description = "Addmission Stages"
    _order = "sequence"

    name = fields.Char()
    sequence = fields.Integer(default=10)  # oreder the stage col.
    fold = fields.Boolean()  # for Kanban
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [
            ("new", "Requested"),
            ("open", "Review"),
            ("done", "Confirm"),
        ],
        default="new",
    )
