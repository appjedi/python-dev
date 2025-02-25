import psycopg2

# Database connection parameters
DB_CONFIG = {
    "dbname": "training",
    "user": "postgres",
    "password": "Test1234",
    "host": "localhost",
    "port": 5432
}

def getConn():
# Connect to PostgreSQL
    return psycopg2.connect(**DB_CONFIG)


def stetup():
# Create a table
    conn=getConn()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE
        )
    """)
    conn.commit()

def insertUser(nm,em):
    # Insert data
    conn=getConn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (nm,em))
    conn.commit()

def listUsers():
# Query data
    conn=getConn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close connection
    cursor.close()
    conn.close()

#insertUser("Mickey Moust","mickey@moust.com")
listUsers()