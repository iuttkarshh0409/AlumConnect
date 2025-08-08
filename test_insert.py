import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def test_db_insert():
    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cursor = conn.cursor()

        # Sample data to insert
        name = "Test User"
        email = "testuser@example.com"
        password_hash = "hashed_password"  # Just a string here for testing
        role = "student"

        # Insert statement
        sql = "INSERT INTO users (name, email, password_hash, role) VALUES (%s, %s, %s, %s)"
        values = (name, email, password_hash, role)

        cursor.execute(sql, values)
        conn.commit()

        print("Insert successful! Last inserted ID:", cursor.lastrowid)
    
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    test_db_insert()
