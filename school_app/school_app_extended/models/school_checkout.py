from odoo import api, exceptions, fields, models
from odoo.exceptions import ValidationError


class Checkout(models.Model):
    _name = "school.checkout"
    _description = "Checkout Request"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    @api.model
    def _default_stage(self):
        Stage = self.env["school.addmission.stage"]
        return Stage.search([("state", "=", "new")], limit=1)

    @api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([], order=order)

    name = fields.Char(string="Title")

    member_id = fields.Many2one("student.registration", "Student name", required=True)
    user_id = fields.Many2one(
        "res.users", "Manager", default=lambda s: s.env.user
    )  # TEACHER

    line_ids = fields.One2many(
        "department.checkout.line",
        "checkout_id",
        string="Notice",
    )

    request_date = fields.Date(
        default=lambda s: fields.Date.today(),
        readonly=False,
    )

    stage_id = fields.Many2one(
        "school.addmission.stage",
        default=_default_stage,
        copy=False,
        group_expand="_group_expand_stage_id",
    )
    state = fields.Selection(related="stage_id.state")

    kanban_state = fields.Selection(
        [
            ("normal", "In Progress"),
            ("blocked", "Blocked"),
            ("done", "Ready for next stage"),
        ],
        "Kanban State",
        default="normal",
    )

    color = fields.Integer()

    priority = fields.Selection(
        [("0", "High"), ("1", "Very High"), ("2", "Critical")], default="0"
    )

    checkout_date = fields.Date(readonly=True)
    close_date = fields.Date(readonly=True)

    # num_books = fields.Integer(compute="_compute_num_books", store=True)

    # @api.depends("line_ids")
    # def _compute_num_books(self):
    #     for book in self:
    #         book.num_books = len(book.line_ids)

    def button_done(self):
        Stage = self.env["school.addmission.stage"]
        done_stage = Stage.search([("state", "=", "done")], limit=1)
        for checkout in self:
            checkout.stage_id = done_stage
        return True
