from odoo import api, exceptions, fields, models


class CheckoutLine(models.Model):
    _name = "department.checkout.line"
    _description = "Checkout Request Line"

    # line model
    checkout_id = fields.Many2one("department.detail", required=True)
    teacher_id = fields.Many2one("teacher.detail", required=True)
    note = fields.Char("Extra Notes")
