import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.schema import ForeignKey


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'postgresql://postgres:1234@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

lists = db.Table(
    'students_courses',
    db.Column('students', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('courses', db.Integer, db.ForeignKey('courses.id'), primary_key=True),
    )


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key = True)
    courses_name = db.Column(db.String(100))
    
    def __repr__(self):
        return f'< {self.courses_name}>'
    

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    lists = db.relationship(
        'Course',
        lazy='dynamic',
        secondary=lists,
        backref=db.backref('students', lazy='dynamic'),
        )
    
    def __repr__(self):
        return f'<{self.id},{self.first_name},{self.last_name},{self.courses_id}>'
    

@app.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)


@app.route('/inform/')
def inform():
    students = Student.query.all()
    return render_template('inform.html', students=students)


@app.route('/<int:id>/',methods=('GET', 'POST'))
def courses(id):
    courses = Course.query.get_or_404(id)
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        student = Student.query.filter_by(
            first_name=first_name,
            last_name=last_name,
            ).first()
        if not student:
            student = Student(first_name=first_name,
                          last_name=last_name
                          )
        db.session.add(student)
        db.session.commit()
        student.lists.append(courses)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('inform'))
    return render_template('courses.html', courses=courses)
    