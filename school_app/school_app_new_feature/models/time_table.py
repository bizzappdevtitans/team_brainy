from odoo import fields, models, api, exceptions


class TimeTable(models.Model):

    _name = "time.table"
    _description = "Time Table"

    time_id = fields.Many2one("faculty.schedual", required=True)

    sub = fields.Selection(
        [
            ("sci", "Science & Technology"),
            ("maths", "Mathematics"),
            ("social", "Social Science"),
            ("guj", "Gujrati"),
            ("pt", "Sports"),
            ("hindi", "Hindi"),
        ],
        string="Subject",
        default="sci",
    )

    weekdays = fields.Selection(
        [
            ("mon", "Monday"),
            ("tue", "Tuesday"),
            ("wed", "Wednesday"),
            ("thus", "Thursday"),
            ("fri", "Friday"),
            ("sat", "Saturday"),
        ],
        string="Weekdays",
        default="mon",
    )

    class_name = fields.Integer("Class")
    div = fields.Selection(
        [
            ("a", "A"),
            ("b", "B"),
            ("c", "C"),
            ("d", "D"),
        ],
        string="Division",
        default="a",
    )

    start_time = fields.Float(string="Start Time")
    end_time = fields.Float(string="End Time")
