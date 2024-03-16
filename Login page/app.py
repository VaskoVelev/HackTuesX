from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'boyan_hristov'

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, email TEXT, password TEXT)')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/loginfail')
def loginfail():
    return render_template('loginfail.html')

@app.route('/signinfail')
def signinfail():
    return render_template('signinfail.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/game')
def game():
    return redirect('http://127.0.0.1:5501/Game/build/web/index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cur.fetchone()

    if existing_user:
        conn.close()
        return redirect('/signinfail')

    try:
        cur.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
    except:
        conn.rollback()

    conn.close()

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
    user = cur.fetchone()
    conn.close()

    if user:
        username = user['username']
        with open('username.txt', 'w') as file:
            file.write(str(username))

        with open('username.txt', 'r') as file:
            print(f"User playing: {str(file.read())}")

        return redirect('/game')
    
    return redirect('/loginfail')

if __name__ == '__main__':
    app.run(debug=True)