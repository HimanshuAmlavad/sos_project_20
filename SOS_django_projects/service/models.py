from time import sleep

from django.db import models
from django.forms.models import model_to_dict


class DropdownItem(models.Model):
    """Abstract base class for dropdown support"""

    class Meta:
        abstract = True  # 🔥 VERY IMPORTANT

    def get_key(self):
        return self.id

    def get_value(self):
        raise NotImplementedError("Subclasses must implement get_value()")

    def to_json(self):
        return model_to_dict(self)


class Role(DropdownItem):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def get_value(self):
        return self.name

    class Meta:
        db_table = "SOS_ROLE"


class User(DropdownItem):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    login = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    dob = models.DateField(null=True, blank=True)
    role_id = models.IntegerField()
    role_Name = models.CharField(max_length=50, blank=True)
    mobileNumber = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, default="Male")
    photo = models.CharField(max_length=200, blank=True, default="")

    @property
    def is_authenticated(self):
        return True

    def get_value(self):
        return f"{self.firstName} {self.lastName}"

    class Meta:
        db_table = "SOS_USER"


class College(DropdownItem):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)

    def get_value(self):
        return self.name

    class Meta:
        db_table = "SOS_COLLEGE"


class Course(DropdownItem):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def get_value(self):
        return self.name

    def to_json(self):
        data = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "duration": self.duration,
        }
        return data

    class Meta:
        db_table = "SOS_COURSE"


class Faculty(DropdownItem):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    mobileNumber = models.CharField(max_length=20)
    address = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=50)
    dob = models.DateField(null=True, blank=True)
    college_ID = models.IntegerField(blank=True, default=0)
    collegeName = models.CharField(max_length=50, blank=True)
    subject_ID = models.IntegerField(blank=True, default=0)
    subjectName = models.CharField(max_length=50, blank=True)
    course_ID = models.IntegerField(blank=True, default=0)
    courseName = models.CharField(max_length=50, blank=True)

    def get_value(self):
        return f"{self.firstName} {self.lastName}"

    class Meta:
        db_table = "SOS_FACULTY"


class Marksheet(DropdownItem):
    rollNumber = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    maths = models.IntegerField()
    year = models.IntegerField()
    student_id = models.IntegerField()

    def get_value(self):
        return f"{self.name} - {self.rollNumber}"

    @property
    def total(self):
        return self.physics + self.chemistry + self.maths

    @property
    def percentage(self):
        return round((self.total / 300) * 100, 2)

    class Meta:
        db_table = "SOS_MARKSHEET"


class Student(DropdownItem):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dob = models.DateField(null=True, blank=True)
    mobileNumber = models.CharField(max_length=20)
    email = models.EmailField()
    college_ID = models.IntegerField()
    collegeName = models.CharField(max_length=50, blank=True)

    def get_value(self):
        return f"{self.firstName} {self.lastName}"

    class Meta:
        db_table = "SOS_STUDENT"


class Subject(DropdownItem):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    dob = models.DateField(null=True, blank=True)
    course_ID = models.IntegerField(default=0)
    courseName = models.CharField(max_length=50, blank=True)

    def get_value(self):
        return self.name

    @property
    def course_name(self):
        return self.courseName

    class Meta:
        db_table = "SOS_SUBJECT"
        unique_together = ("name", "course_ID")


class TimeTable(DropdownItem):
    exam_date = models.DateField(null=True, blank=True)
    exam_time = models.CharField(max_length=50)
    subject_id = models.IntegerField(default=0)
    subject_name = models.CharField(max_length=50, blank=True)
    course_id = models.IntegerField(default=0)
    course_name = models.CharField(max_length=50, blank=True)
    semester = models.CharField(max_length=50)

    def get_value(self):
        return f"{self.course_name} - {self.subject_name} - {self.exam_date} {self.exam_time}"

    class Meta:
        db_table = "SOS_TIMETABLE"

from django.db import models


class Parking(models.Model):
    parking_id = models.IntegerField()
    parking_code = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=20)
    slot_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "sos_parking"

    # def get_key(self):
    #     return self.parkingid

    # def get_value(self):
    #     return self.parking_code


class Drone(models.Model):
    drone_id = models.IntegerField()
    drone_code = models.CharField(max_length=50)
    operator_name = models.CharField(max_length=20)
    delivery_zone = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "sos_drone"

    # def get_key(self):
    #     return self.drone_id

    # def get_value(self):
    #     return self.drone_code


class WeatherAlert(models.Model):
    alert_id = models.IntegerField()
    alert_code = models.CharField(max_length=50)
    city_name = models.CharField(max_length=50)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=30)

    class Meta:
        db_table = "weather_alert"


class VoiceCommand(models.Model):
    command_id = models.IntegerField()
    command_code = models.CharField(max_length=50)
    user_name = models.CharField(max_length=100)
    command_text = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    class Meta:
        db_table = "voice_command"

    # def get_value(self):
    #     return self.command_code


class Employee(models.Model):
    employee_id = models.IntegerField()
    employee_code = models.CharField(max_length=20, unique=True)
    employee_Name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "employee"

    # def get_value(self):
    #     return self.employee_code



class Book(models.Model):
    book_id = models.IntegerField()
    book_code = models.CharField(max_length=20, unique=True)
    book_title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "book"

    # def get_value(self):
    #     return self.book_id


class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    movie_code = models.CharField(max_length=20, unique=True)
    movie_name = models.CharField(max_length=100)
    director_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "movie"



class Vehicle(models.Model):
    vehicle_id = models.IntegerField()
    vehicle_no = models.CharField(max_length=20, unique=True)
    model_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    class Meta:
        db_table = "vehicle"


class Department(models.Model):

    department_id = models.IntegerField()
    department_code = models.CharField(max_length=20, unique=True)
    department_name = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "department"


class Fee(models.Model):

    fee_id = models.IntegerField(unique=True)
    student_id = models.CharField(max_length=20,unique=True)
    amount = models.IntegerField()
    payment_date = models.DateField()
    payment_status = models.CharField(max_length=20)

    class Meta:
        db_table = "fee"

class Scholarship(models.Model):

    scholarship_id = models.IntegerField(unique=True)
    scholarship_name = models.CharField(max_length=100)
    amount = models.IntegerField(max_length=15)
    eligibility = models.CharField(max_length=255)
    last_date = models.DateField()

    class Meta:
        db_table = "scholarship"

class Attendance(models.Model):

    attendance_id = models.IntegerField(unique=True)
    student_id = models.IntegerField(unique=True)
    student_name = models.CharField(max_length=100)
    attendance_date = models.DateField()
    student_class = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "attendance"

class Branch(models.Model):

    branch_id = models.IntegerField(unique=True)
    branch_name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=15, unique=True)

    class Meta:
        db_table ="branch"

class Result(models.Model):

    result_id = models.IntegerField(unique=True)
    student_id = models.CharField(max_length=20, unique=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=1)
    grade = models.CharField(max_length=5)
    status = models.CharField(max_length=20)

    class Meta:
        db_table ="result"

class CreditCard(models.Model):

    card_id = models.IntegerField(unique=True)
    card_number = models.CharField(max_length=16, unique=True)
    card_holder = models.CharField(max_length=100)
    expiry_date = models.DateField()
    card_type = models.CharField(max_length=50)

    class Meta:
        db_table = "creditcard"

class ATM(models.Model):

    atm_id = models.IntegerField(unique=True)
    location = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    cash_available = models.IntegerField()
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "atm"

class Product(models.Model):
    product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=100)

    class Meta:
        db_table = "product"

class Order(models.Model):

    order_id = models.IntegerField(unique=True)
    order_date = models.DateField()
    amount = models.IntegerField()
    status = models.CharField(max_length=20)
    customer_id = models.IntegerField()

    class Meta:
        db_table = "order"