from flask import Flask, render_template, request
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# This initialization correctly points to your templates and static folders
app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

def get_db_connection():
    """Establishes a connection to the database."""
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return conn

@app.route('/')
def home():
    """Renders the main landing page."""
    return render_template('homepage.html')

@app.route('/student')
def student_dashboard():
    """Fetches and displays the full alumni list for students."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM alumni;')
    alumni_list = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('student.html', alumni=alumni_list)

@app.route('/alumni')
def alumni_dashboard():
    """Fetches and displays the full alumni list for alumni."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM alumni;')
    alumni_list = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('alumni.html', alumni=alumni_list)

@app.route('/search', methods=['POST'])
def search():
    """Handles the search form submission."""
    query = request.form['query']
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    search_pattern = f"%{query}%"
    
    cursor.execute(
        "SELECT * FROM alumni WHERE name LIKE %s OR role LIKE %s OR company LIKE %s OR domain LIKE %s",
        (search_pattern, search_pattern, search_pattern, search_pattern)
    )
    
    search_results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Renders the search results on the student page.
    return render_template('student.html', alumni=search_results)

if __name__ == '__main__':
    app.run(debug=True)