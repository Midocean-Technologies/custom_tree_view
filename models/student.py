from odoo import api, fields, models


class Student(models.Model):
    _name = "student"
    _description = "Student"
    _rec_name = "EnrollmentNo"

    EnrollmentNo = fields.Char(string="Enrollment_Number")
    name = fields.Char(string="Name")
    email = fields.Char(string="email_address")
    dob = fields.Date(string="Date_Of_Birth")
    ph_no = fields.Char(string="Phone_Number")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], String="Gender")
