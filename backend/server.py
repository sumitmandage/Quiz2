# from flask import Flask, jsonify, Response
# from flask_cors import CORS
# from models import db, seed_data, Employee, Department, Performance, Attendance, seed_data
# import csv
# import random
# from faker import Faker

# app = Flask(__name__)
# CORS(app)

# # Replace with your actual MySQL username/password/db
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/employee_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db.init_app(app)

# with app.app_context():
#     db.create_all()
#     if not Employee.query.first():
#         seed_data(db)
    

# @app.route("/")
# def home():
#     return {"message": "Employee API Running"}

# @app.route("/employees")
# def get_employees():
#     employees = Employee.query.all()
#     data = [{
#         "id": e.id,
#         "name": e.name,
#         "email": e.email,
#         "department": e.department.name,
#         "joining_date": e.joining_date.strftime("%Y-%m-%d"),
#         "salary": e.salary
#     } for e in employees]
#     return jsonify(data)

# @app.route("/performance-summary")
# def performance_summary():
#     all_perf = Performance.query.all()
#     scores = {}
#     for p in all_perf:
#         name = Employee.query.get(p.employee_id).name
#         scores.setdefault(name, []).append(p.score)

#     avg_scores = {name: round(sum(scores_list) / len(scores_list), 2)
#                   for name, scores_list in scores.items()}
#     return jsonify(avg_scores)


# @app.route('/attendance', methods=['GET'])
# def get_attendance():
#     records = Attendance.query.all()
#     data = [{
#         "id": a.id,
#         "employee_id": a.employee_id,
#         "employee_name": a.employee.name,
#         "date": a.date.strftime('%Y-%m-%d'),
#         "status": a.status
#     } for a in records]
#     return jsonify(data)


# @app.route('/performance', methods=['GET'])
# def get_performance():
#     records = Performance.query.all()
#     data = [{
#         "id": p.id,
#         "employee_id": p.employee_id,
#         "employee_name": p.employee.name,  # relationship must be defined in models.py
#         "date": p.date.strftime('%Y-%m-%d'),
#         "score": p.score,
#         "feedback": p.feedback
#     } for p in records]
#     return jsonify(data)


# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, jsonify, Response
from flask_cors import CORS
from models import db, seed_data, Employee, Department, Performance, Attendance
import csv

app = Flask(__name__)
CORS(app)

# ✅ Replace with your actual MySQL credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/employee_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ✅ Seed database only if empty
with app.app_context():
    db.create_all()
    if not Employee.query.first():
        seed_data(db)

@app.route("/")
def home():
    return {"message": "Employee API Running"}

@app.route("/employees")
def get_employees():
    employees = Employee.query.all()
    data = [{
        "id": e.id,
        "name": e.name,
        "email": e.email,
        "department": e.department.name if e.department else "N/A",
        "joining_date": e.joining_date.strftime("%Y-%m-%d"),
        "salary": e.salary
    } for e in employees]
    return jsonify(data)

@app.route("/performance-summary")
def performance_summary():
    all_perf = Performance.query.all()
    scores = {}
    for p in all_perf:
        name = p.employee.name
        scores.setdefault(name, []).append(p.score)

    avg_scores = {
        name: round(sum(score_list) / len(score_list), 2)
        for name, score_list in scores.items()
    }
    return jsonify(avg_scores)

@app.route('/attendance', methods=['GET'])
def get_attendance():
    records = Attendance.query.all()
    data = [{
        "id": a.id,
        "employee_id": a.employee_id,
        "employee_name": a.employee.name,
        "date": a.date.strftime('%Y-%m-%d'),
        "status": a.status
    } for a in records]
    return jsonify(data)

@app.route('/performance', methods=['GET'])
def get_performance():
    records = Performance.query.all()
    data = [{
        "id": p.id,
        "employee_id": p.employee_id,
        "employee_name": p.employee.name,
        "review_date": p.review_date.strftime('%Y-%m-%d'),
        "score": p.score,
        "remarks": p.remarks
    } for p in records]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
