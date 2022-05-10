import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.schema import ForeignKey


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'postgresql://postgres:1234@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Courses(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    courses_name = db.Column(db.String(100))
    
    def __repr__(self):
        return f'< {self.courses_name}>'
    
    
class Students(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    students_id = db.Column(db.Integer,db.ForeignKey(Courses.id))
    
    def __repr__(self):
        return f'<{self.id},{self.firstname},{self.lastname},{self.students_id}>'
    
    
@app.route('/')
def index():
    courses = Courses.query.all()
    return render_template('index.html', courses=courses)


@app.route('/inform/')
def inform():
    students = Students.query.join(Courses,Students.students_id==Courses.id).all()
    return render_template('inform.html', students=students)


@app.route('/<int:id>/',methods=('GET', 'POST'))
def courses(id):
    courses = Courses.query.get_or_404(id)
    if request.method == 'POST':
        courses_name = id
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        student = Students(firstname=firstname,
                          lastname=lastname,
                          students_id=courses_name)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('inform'))
    return render_template('courses.html', courses=courses)
    