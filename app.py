import sqlite3
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


# ==============================
# DATABASE CONNECTION
# ==============================

def get_db_connection():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn


# ==============================
# HOME PAGE
# ==============================

@app.route('/')
def home():
    return render_template('index.html')


# ==============================
# EXISTING STUDENT API
# ==============================

@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "24-00102",
        "name": "Noeme Defacto",
        "program": "BSIT",
        "year": 3,
        "section": "Dijsktra"
    })


# ==============================
# GREETING API
# ==============================

@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Student')

    return jsonify({
        "message": f"Hello, {name}!"
    })


# ==============================
# CUSTOM COURSE API
# ==============================

@app.route('/course')
def get_course():
    return jsonify({
        "course_code": "IT 3120",
        "course_title": "System Integration",
        "instructor": "Dr. Rene Arduo"
    })


# ==============================
# DATABASE API
# GET ALL STUDENTS
# ==============================

@app.route('/students')
def get_students():
    conn = get_db_connection()

    students = conn.execute(
        'SELECT * FROM students'
    ).fetchall()

    conn.close()

    return jsonify([dict(student) for student in students])


# ==============================
# DATABASE API
# GET ONE STUDENT BY ID
# ==============================

@app.route('/students/<int:id>')
def get_student_by_id(id):
    conn = get_db_connection()

    student = conn.execute(
        'SELECT * FROM students WHERE id = ?',
        (id,)
    ).fetchone()

    conn.close()

    if student is None:
        return jsonify({
            "error": "Student not found"
        }), 404

    return jsonify(dict(student))


# ==============================
# ADDITIONAL DATABASE API
# GET STUDENTS BY PROGRAM
# ==============================

@app.route('/students/program/<program>')
def get_students_by_program(program):
    conn = get_db_connection()

    students = conn.execute(
        'SELECT * FROM students WHERE program = ?',
        (program,)
    ).fetchall()

    conn.close()

    return jsonify([dict(student) for student in students])


# ==============================
# RUN APPLICATION
# ==============================

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )