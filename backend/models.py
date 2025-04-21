# from flask_sqlalchemy import SQLAlchemy
# from faker import Faker
# from datetime import datetime, timedelta
# import random

# db = SQLAlchemy()
# fake = Faker()

# class Department(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)

# class Employee(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     email = db.Column(db.String(100), unique=True)
#     department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
#     joining_date = db.Column(db.Date)
#     salary = db.Column(db.Float)

#     department = db.relationship('Department', backref=db.backref('employees', lazy=True))

# class Attendance(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
#     date = db.Column(db.Date)
#     status = db.Column(db.String(10))  # Present or Absent

#     employee = db.relationship('Employee', backref='attendances')


# # class Performance(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
# #     review_date = db.Column(db.Date)
# #     score = db.Column(db.Integer)
# #     remarks = db.Column(db.String(255))

# # def seed_data(db):
# #     departments = ['Engineering', 'HR', 'Sales']
# #     for name in departments:
# #         db.session.add(Department(name=name))
# #     db.session.commit()

# #     for _ in range(5):
# #         emp = Employee(
# #             name=fake.name(),
# #             email=fake.unique.email(),
# #             department_id=random.randint(1, 3),
# #             joining_date=fake.date_between(start_date='-2y', end_date='today'),
# #             salary=round(random.uniform(30000, 100000), 2)
# #         )
# #         db.session.add(emp)
# #         db.session.commit()

# #         for _ in range(5):
# #             db.session.add(Attendance(
# #                 employee_id=emp.id,
# #                 date=fake.date_between(start_date='-30d', end_date='today'),
# #                 status=random.choice(['Present', 'Absent'])
# #             ))
# #             db.session.add(Performance(
# #                 employee_id=emp.id,
# #                 review_date=fake.date_between(start_date='-1y', end_date='today'),
# #                 score=random.randint(1, 10),
# #                 remarks=fake.sentence()
# #             ))
# #         db.session.commit()


# class Performance(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
#     review_date = db.Column(db.Date)
#     score = db.Column(db.Integer)
#     remarks = db.Column(db.String(255))

#     employee = db.relationship('Employee', backref='performances')

from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import random

db = SQLAlchemy()
fake = Faker()

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    joining_date = db.Column(db.Date)
    salary = db.Column(db.Float)

    department = db.relationship('Department', backref=db.backref('employees', lazy=True))

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    date = db.Column(db.Date)
    status = db.Column(db.String(10))  # Present or Absent

    employee = db.relationship('Employee', backref='attendances')

class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    review_date = db.Column(db.Date)
    score = db.Column(db.Integer)
    remarks = db.Column(db.String(255))

    employee = db.relationship('Employee', backref='performances')

# ✅ This function is outside the class — correct location
def seed_data(db):
    departments = ['Engineering', 'HR', 'Sales']
    for name in departments:
        db.session.add(Department(name=name))
    db.session.commit()

    for _ in range(5):
        emp = Employee(
            name=fake.name(),
            email=fake.unique.email(),
            department_id=random.randint(1, 3),
            joining_date=fake.date_between(start_date='-2y', end_date='today'),
            salary=round(random.uniform(30000, 100000), 2)
        )
        db.session.add(emp)
        db.session.commit()

        for _ in range(5):
            db.session.add(Attendance(
                employee_id=emp.id,
                date=fake.date_between(start_date='-30d', end_date='today'),
                status=random.choice(['Present', 'Absent'])
            ))
            db.session.add(Performance(
                employee_id=emp.id,
                review_date=fake.date_between(start_date='-1y', end_date='today'),
                score=random.randint(1, 10),
                remarks=fake.sentence()
            ))
        db.session.commit()
