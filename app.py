from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


# ==============================
# HOME PAGE
# ==============================

@app.route('/')
def home():
    return render_template('index.html')


# ==============================
# STUDENT API
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
# RUN APPLICATION
# ==============================

if __name__ == '__main__':
    app.run(debug=True)