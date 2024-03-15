from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to something secure in production

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database
def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, email TEXT, password TEXT)')
    conn.commit()
    conn.close()

# Initialize the database if not exists
init_db()

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/facts.html')
def fact():
    return render_template('facts.html')

@app.route('/loginfail.html')
def testfail():
    return render_template('loginfail.html')

@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')

# Route for registration
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

    # Check if the username already exists in the database
    cur.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cur.fetchone()

    if existing_user:
        conn.close()
        return redirect('/loginfail')

    # If the username is unique, proceed with registration
    try:
        cur.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        flash('Registration successful! Please log in.')
    except:
        conn.rollback()
        flash('An error occurred during registration. Please try again.')

    conn.close()

    return redirect('/game')

# Route for login
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
        return redirect('/game')
    
    return redirect('/loginfail')

if __name__ == '__main__':
    app.run(debug=True)