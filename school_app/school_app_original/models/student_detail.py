from odoo import fields, models, api, exceptions
from datetime import datetime, date
from dateutil.relativedelta import *
from odoo import _

try:
    from collections.abc import Callable
except ImportError:
    from collections import Callable


class Student(models.Model):
    """
    Describes a Students Deails.
    """

    _name = "student.detail"
    _description = "student detail"

    name = fields.Char(
        string="Student Number", readonly=True, required=True, copy=False, default="New"
    )
    fname = fields.Char("First Name", required=True)
    mname = fields.Char("Middel Name", required=True)
    lname = fields.Char("Last Name", required=True)
    _rec_name = "fname"
    date_of_birth = fields.Date()

    @api.constrains("date_of_birth")
    def _check_date_of_birth(self):
        for record in self:
            if record.date_of_birth > fields.Date.today():
                raise ValidationError("The Birth date cannot be set in the future")

    age = fields.Integer(string="Age")

    @api.onchange("date_of_birth")
    def _onchange_birth_date(self):
        if self.date_of_birth:
            d1 = datetime.strptime(str(self.date_of_birth), "%Y-%m-%d").date()
            d2 = date.today()
            self.age = relativedelta(d2, d1).years

    address = fields.Text("Adrress")
    roll_number = fields.Integer("Roll Number")

    act_id = fields.Integer(string="Activity ID")
    level = fields.Char("Level")

    # @api.constrains("act_id")
    # def _check_activity(self):
    #     if self.act_id not in (self.env["department.detail"].browse("ids")):
    #         raise ValidationError("%s ID is must be equal to department id")

    # error ->>TypeError: unsupported operand type(s) for "in": 'department.detail()' and '<class 'int'>'

    phone_number_s = fields.Char("Student's Contact Number")
    phone_number_p = fields.Char("Parent's Contact Number")

    occupation = fields.Char("Parent's Occupation")

    meadium = fields.Selection(
        [("english", "English"), ("hindi", "Hindi"), ("gujrati", "Gujrati")],
        "Meadium",
        default="english",
    )

    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other")],
        "Female",
        default="female",
    )

    image = fields.Binary("Passport Photo")
    color = fields.Integer("Fevorite Colour")
    email = fields.Char("Student MailID")

    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("in_progress", "In Progress"),
            ("cancel", "Cancelled"),
            ("done", "Done"),
        ],
        string="Status",
        required=True,
        readonly=True,
        copy=False,
        default="draft",
    )

    def button_in_progress(self):
        self.write({"state": "in_progress"})

    sports = fields.Selection(
        [
            ("tt", "Table Tanis"),
            ("bb", "Basket Ball"),
            ("ck", "Cricket"),
            ("ch", "Chess"),
        ],
        "Sports",
        default="tt",
    )

    activity = fields.Selection(
        [("id", "Indore Activity"), ("od", "Outdoor Activity")],
        "Activity",
    )

    addmission_request_date = fields.Date(
        default=lambda s: fields.Date.today(),
    )

    @api.constrains("phone_number_s")
    def _constrain_phone_number_s_valid(self):
        for student in self:
            if student.phone_number_s and not student._check_phone_number_s():
                raise ValidationError(
                    "%s is an invalid phone_number" % student.phone_number_s
                )

    def _check_phone_number_s(self):
        self.ensure_one()
        digits = [int(x) for x in self.phone_number_s if x.isdigit()]
        if len(digits) == 10:
            return digits

    @api.constrains("phone_number_p")
    def _constrain_phone_number_p_valid(self):
        for student in self:
            if student.phone_number_p and not student._check_phone_number_p():
                raise ValidationError(
                    "%s is an invalid phone_number" % student.phone_number_p
                )

    def _check_phone_number_p(self):
        # self.ensure_one()
        digits = [int(x) for x in self.phone_number_p if x.isdigit()]
        if len(digits) == 10:
            return digits

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code("student.detail")
        return super(Student, self).create(vals)

    grade = fields.Char("Grades")

    # @api.onchange("total_marks")
    # def _check_grades(self):
    #     if self.total_marks > 90:
    #         self.grade == "AA"
    #     return self.grade
