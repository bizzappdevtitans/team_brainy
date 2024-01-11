from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    custom_emails = fields.Char(
        "Custom Emails", config_parameter="my_module.custom_emails"
    )
