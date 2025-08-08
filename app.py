import logging
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.secret_key = 'a_random_secret_key'  # Keep this secret in production!

# Set up logging
logging.basicConfig(filename='app_errors.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')


def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return conn


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/student')
def student_dashboard():
    # Restrict access to logged-in students only
    if 'user_role' not in session or session['user_role'] != 'student':
        flash('Please log in as a student to access this page.', 'warning')
        return redirect(url_for('home'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM alumni;')
    alumni_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('student.html', alumni=alumni_list)


@app.route('/alumni')
def alumni_dashboard():
    # Restrict access to logged-in alumni only
    if 'user_role' not in session or session['user_role'] != 'alumni':
        flash('Please log in as an alumni to access this page.', 'warning')
        return redirect(url_for('home'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM alumni;')
    alumni_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('alumni.html', alumni=alumni_list)


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']

    password_hash = generate_password_hash(password)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, password_hash, role) VALUES (%s, %s, %s, %s)",
            (name, email, password_hash, role)
        )
        conn.commit()
        flash('Registration successful! Please log in.', 'success')
    except mysql.connector.Error as err:
        logging.error(f"Database error during registration: {err}", exc_info=True)
        flash(f"An error occurred: {err}", 'danger')
    except Exception as ex:
        logging.error(f"Unexpected error during registration: {ex}", exc_info=True)
        flash(f"An unexpected error occurred. Please try again later.", 'danger')
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

    return redirect(url_for('home'))


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        flash('Please enter email and password.', 'danger')
        return redirect(url_for('home'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user and check_password_hash(user['password_hash'], password):
        # Successful login: store user info in session
        session['user_id'] = user['id']
        session['user_role'] = user['role']
        flash('Login successful!', 'success')

        # Redirect based on role
        if user['role'] == 'student':
            return redirect(url_for('student_dashboard'))
        elif user['role'] == 'alumni':
            return redirect(url_for('alumni_dashboard'))
        else:
            flash('User role unknown. Contact support.', 'danger')
            return redirect(url_for('home'))
    else:
        flash('Invalid email or password.', 'danger')
        return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))


if __name__ == '__main__':
     app.run(debug=True)
