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

@app.route('/aboutus.html')
def aboutus():
    return render_template('aboutus.html')

# Route for registration
@app.route('/register', methods=['POST'])
def register():
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        conn.close()

        flash('Registration successful! Please log in.')
    except sqlite3.IntegrityError:
        flash('Username or email already exists. Please choose a different one.')
    return redirect('/')

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
        flash('Login successful!')
    else:
        flash('Invalid email or password.')

    #return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)