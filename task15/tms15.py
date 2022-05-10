import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='postgres',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = int(request.form['year'])
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO books (title, author, year) VALUES (%s, %s, %s)',(title, author, year))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/delete/', methods=('GET', 'POST'))
def delete():
    if request.method == 'POST':
        author = str(request.form['author'])
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''DELETE from  books where author = '{}';'''.format(author))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('delete.html')

#DB_USERNAME = postgres
#DB_PASSWORD = 1234
    
