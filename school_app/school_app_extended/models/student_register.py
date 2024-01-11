from odoo import fields, models, api, exceptions
from odoo.exceptions import ValidationError
from datetime import datetime, date, timedelta


class Registration(models.Model):

    _name = "student.registration"
    _description = "student registration"

    name = fields.Char("Name", required=True)
    email = fields.Char("Email")

    # header model
    line_id_one = fields.One2many(
        "general.detail",
        "reg_id",
        string="General",
    )

    line_id_two = fields.One2many(
        "medical.detail",
        "med_id",
        string="medical",
    )

    line_id_three = fields.One2many(
        "contact.detail",
        "con_id",
        string="contact",
    )

    line_id_four = fields.One2many(
        "academic.detail",
        "acm_id",
        string="Academic",
    )

    line_id_five = fields.One2many(
        "remark.detail",
        "rem_id",
        string="Remarks",
    )

    registration_date = fields.Date("Registration Date", required=True)
    preparation_days = fields.Integer("Days Remaining For Preparation")

    interview_date = fields.Date(
        string="Interview Date",
        default=fields.datetime.now(),
        compute="_compute_interview_date",
        inverse="_inverse_interview_date",
    )

    @api.depends("registration_date")
    def _compute_interview_date(self):
        for student in self:
            if student.registration_date:
                student.interview_date = student.registration_date + timedelta(
                    days=student.preparation_days
                )

    def _inverse_interview_date(self):
        if self.interview_date:
            self.preparation_days = (self.interview_date - self.registration_date).days
        pass

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("started", "Started"),
            ("progress", "In progress"),
            ("finished", "Done"),
        ],
        default="draft",
    )

    def draft_progressbar(self):
        self.write(
            {
                "state": "draft",
            }
        )

    # This function is triggered when the user clicks on the button 'Set to started'

    def started_progressbar(self):
        self.write({"state": "started"})

    # This function is triggered when the user clicks on the button 'In progress'

    def progress_progressbar(self):
        self.write({"state": "progress"})

    # This function is triggered when the user clicks on the button 'Done'

    def done_progressbar(self):
        self.write(
            {
                "state": "finished",
            }
        )
