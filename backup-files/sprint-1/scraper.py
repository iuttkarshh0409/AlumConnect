# Import necessary libraries for web scraping, browser automation, and database connection
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector
import traceback

def main():
    # Define the target URL for the alumni registration page
    target_url = "https://iips.edu.in/alumni_reg.php"
    
    print(f"Connecting to {target_url}...")
    try:
        # Initialize the Chrome WebDriver automatically
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # Navigate to the target URL
        driver.get(target_url)
        
        # Find the "Alumni List" link by its unique onclick JavaScript function
        print("Clicking on 'Alumni List'...")
        alumni_list_link = driver.find_element(By.XPATH, "//a[contains(@onclick, \"alumni_get('list')\")]")
        # Simulate a click on the link to load the alumni data
        alumni_list_link.click()

        # Wait for a maximum of 10 seconds for the main content container to become visible
        print("Waiting for alumni table to load...")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "detail")))
        print("Alumni table loaded.")

        # Get the HTML source of the page *after* the content has been loaded
        html_source = driver.page_source
        # Close the browser
        driver.quit()
        print("Successfully retrieved final page source.")

    except Exception as e:
        # Catch any errors during the Selenium process and print them
        print("\nAn error occurred with Selenium:")
        print(traceback.format_exc())
        return

    # Proceed only if the HTML source was successfully retrieved
    if html_source:
        # Use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(html_source, 'html.parser')
        # Find the main div container that holds all the alumni tables
        main_container = soup.find('div', id='detail')
        
        alumni_data = []
        # Check if the main container was found
        if main_container:
            # Find all tables within the container
            all_tables = main_container.find_all('table', class_='table-hover')
            # Loop through each table
            for table in all_tables:
                # Find all rows in the current table
                rows = table.find_all('tr')
                # Loop through each row, skipping the first one (the header)
                for row in rows[1:]:
                    # Find all cells in the current row
                    cells = row.find_all('td')
                    # Ensure the row has at least 3 cells of data
                    if len(cells) >= 3:
                        # Create a tuple of the cleaned data
                        alumnus = (
                            cells[0].text.strip(), # name
                            cells[1].text.strip(), # role
                            cells[2].text.strip()  # company
                        )
                        # Add the tuple to our list of alumni
                        alumni_data.append(alumnus)

        # Proceed only if alumni data was successfully scraped
        if alumni_data:
            print(f"\nSuccessfully scraped {len(alumni_data)} records.")
            
            try:
                # Connect to the MySQL database using credentials
                print("Connecting to the MySQL database...")
                db_connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Raam@12345",
                    database="alumniDB"
                )
                cursor = db_connection.cursor()
                print("Database connection successful.")
                
                # Define the SQL query to insert data into specific columns
                sql = "INSERT INTO alumni (name, role, company) VALUES (%s, %s, %s)"
                
                # Execute the insert command for all scraped records at once
                cursor.executemany(sql, alumni_data)
                # Commit the changes to the database
                db_connection.commit()
                
                print(f"{cursor.rowcount} records were successfully inserted into the database.")

            except mysql.connector.Error as err:
                # Catch any database-related errors
                print(f"Error connecting to MySQL: {err}")
            finally:
                # Ensure the database connection is closed, even if errors occurred
                if 'db_connection' in locals() and db_connection.is_connected():
                    cursor.close()
                    db_connection.close()
                    print("MySQL connection is closed.")
        else:
            print("Could not find or parse alumni data from the page after the click.")

# Standard Python entry point
if __name__ == "__main__":
    main()