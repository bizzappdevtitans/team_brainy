import logging
from odoo import api, exceptions, fields, models


_logger = logging.getLogger(__name__)


class CheckoutMassMessage(models.TransientModel):
    _name = "teacher.checkout.massmessage"
    _description = "Send Message to teacher"

    checkout_ids = fields.Many2many(
        "teacher.detail",
        string="Check",
    )

    message_subject = fields.Char()
    message_body = fields.Char()

    @api.model
    def default_get(self, field_names):
        defaults_dict = super().default_get(field_names)

        checkout_ids = self.env.context["active_ids"]
        defaults_dict["checkout_ids"] = [(6, 0, checkout_ids)]  # ?
        return defaults_dict

    def button_send(self):
        self.ensure_one()
        if not self.checkout_ids:
            raise exceptions.UserError("No Checkouts were selected.")
        if not self.message_body:
            raise exceptions.UserError("A message body is required")

            _logger.debug(
                "Message on %d to followers: %s",
                checkout.id,
                checkout.message_follower_ids,
            )

        _logger.info(
            "Posted %d messages to the Checkouts: %s",
            len(self.checkout_ids),
            str(self.checkout_ids),
        )
        return True


"""
output: odoo.addons.school_app_original.wizard.checkout_mass_message:
 Posted 5 messages to the Checkouts: teacher.detail(1, 2, 3, 4, 5)
"""
