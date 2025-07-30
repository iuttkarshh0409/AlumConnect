from flask import Flask, render_template, request
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='app/templates',static_folder='app/static')

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
    """Fetches alumni data and renders it on the homepage."""
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
    # Get the search query from the form
    query = request.form['query']
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Create a search pattern for the SQL LIKE clause
    search_pattern = f"%{query}%"
    
    # Execute a query that searches across multiple columns
    cursor.execute(
        "SELECT * FROM alumni WHERE name LIKE %s OR role LIKE %s OR company LIKE %s",
        (search_pattern, search_pattern, search_pattern)
    )
    
    search_results = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Reuse the home.html template to display the search results
    return render_template('alumni.html', alumni=search_results)

if __name__ == '__main__':
    app.run(debug=True)