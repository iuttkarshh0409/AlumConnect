import mysql.connector

def classify_domain(role):
    """
    A more intelligent function to classify a domain based on job title keywords.
    """
    role_lower = role.lower()
    
    # More specific keywords, ordered from most to least specific
    devops_keywords = ['devops']
    hr_keywords = ['hr associate', 'human resources']
    finance_keywords = ['finance', 'equity', 'banker', 'financial analyst']
    marketing_sales_keywords = ['marketing', 'sales', 'business development']
    consultant_keywords = ['consultant', 'tax consultant']
    dev_keywords = ['developer', 'engineer', 'architect', 'swe', 'sde', 'sdet', 'ui developer']
    management_keywords = ['manager', 'director', 'lead', 'analyst', 'head of']
    
    if any(keyword in role_lower for keyword in devops_keywords):
        return 'DevOps'
    if any(keyword in role_lower for keyword in hr_keywords):
        return 'Human Resources'
    if any(keyword in role_lower for keyword in finance_keywords):
        return 'Finance'
    if any(keyword in role_lower for keyword in marketing_sales_keywords):
        return 'Marketing & Sales'
    if any(keyword in role_lower for keyword in consultant_keywords):
        return 'Consulting'
    if any(keyword in role_lower for keyword in dev_keywords):
        return 'Software Development'
    if any(keyword in role_lower for keyword in management_keywords):
        return 'Management/Analyst'
    else:
        return 'General' # Default category

def main():
    try:
        print("Connecting to the MySQL database...")
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Raam@12345",
            database="alumniDB"
        )
        cursor = db_connection.cursor(dictionary=True)
        print("Database connection successful.")
        
        # 1. Fetch all records where domain is NULL or the default 'General'
        cursor.execute("SELECT id, role FROM alumni WHERE domain IS NULL OR domain = 'General'")
        records_to_update = cursor.fetchall()
        print(f"Found {len(records_to_update)} records to classify.")

        updates = []
        for record in records_to_update:
            if record['role']:
                domain = classify_domain(record['role'])
                updates.append((domain, record['id']))
        
        if updates:
            # 2. Prepare and execute the update queries
            sql = "UPDATE alumni SET domain = %s WHERE id = %s"
            cursor.executemany(sql, updates)
            db_connection.commit()
            
            print(f"{cursor.rowcount} records were successfully updated with a new domain.")

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
    finally:
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    main()