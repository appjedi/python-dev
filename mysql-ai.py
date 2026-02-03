import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='$Data2026',
        database='appjedin_student_temp'
    )
    
    if connection.is_connected():
        print("Connected to MySQL database")
        
        # Create a cursor object to interact with the database
        cursor = connection.cursor()
        
        # Execute a query
        cursor.execute("SELECT * FROM users")
        
        # Fetch all results
        results = cursor.fetchall()
        
        # Print rows
        for row in results:
            print(row)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    # Close cursor and connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
