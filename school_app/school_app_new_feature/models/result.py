from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Result(models.Model):
    _name = "result.detail"
    _description = "Marksheet"

    result_id = fields.Many2one("student.detail", required=True)
    name = fields.Many2one("student.detail", string="Name")

    test_no = fields.Integer("Test Number")
    test_date = fields.Date("Test Date")
    maths_marks = fields.Integer("Mathematics")
    science_marks = fields.Integer("Science")
    social_marks = fields.Integer("Social Science")
    english_marks = fields.Integer("English")
    gujarati_marks = fields.Integer("Gujarati")
    hindi_marks = fields.Integer("Hindi")
    drawing_marks = fields.Integer("Drawing")

    total_marks = fields.Integer(string="Total Marks", compute="_compute_total_marks")

    api.depends(
        "maths_marks",
        "social_marks",
        "science_marks",
        "english_marks",
        "gujarati_marks",
        "hindi_marks",
        "drawing_marks",
    )

    def _compute_total_marks(self):
        for marks in self:
            marks.total_marks = (
                marks.maths_marks
                + marks.science_marks
                + marks.social_marks
                + marks.english_marks
                + marks.gujarati_marks
                + marks.hindi_marks
                + marks.drawing_marks
            )
            return marks.total_marks

    test_type = fields.Selection(
        [("weekly", "Weekly Test"), ("monthly", "Monthly Test"), ("Final", "Final")],
        "Test Type",
        default="weekly",
    )

    @api.constrains("maths_marks")
    def _english_marks_valid(self):
        if self.maths_marks > 100:
            raise ValidationError("Enter Your Mathematics Subject Marks out of 100")

    @api.constrains("science_marks")
    def _science_marks_valid(self):
        if self.science_marks > 100:
            raise ValidationError("Enter Your Science Subject Marks out of 100")

    @api.constrains("social_marks")
    def _maths_marks_valid(self):
        if self.social_marks > 100:
            raise ValidationError("Enter Your Social Science Subject Marks out of 100")

    @api.constrains("english_marks")
    def _maths_marks_valid(self):
        if self.english_marks > 100:
            raise ValidationError("Enter Your English Subject Marks out of 100")

    @api.constrains("gujarati_marks")
    def _maths_marks_valid(self):
        if self.gujarati_marks > 100:
            raise ValidationError("Enter Your Gujarati Subject Marks out of 100")

    @api.constrains("hindi_marks")
    def _maths_marks_valid(self):
        if self.hindi_marks > 100:
            raise ValidationError("Enter Your Hindi Subject Marks out of 100")

    @api.constrains("drawing_marks")
    def _maths_marks_valid(self):
        if self.drawing_marks > 100:
            raise ValidationError("Enter Your Drawing Subject Marks out of 100")
