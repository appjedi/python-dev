import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="Test1234",
    host="localhost",
    port="5432"
)

# Create a cursor
cur = conn.cursor()

# Create a table
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
""")

# Insert data
cur.execute("""
    INSERT INTO users (name, email)
    VALUES (%s, %s)
    RETURNING id
""", ("Alice", "alice@example.com"))

user_id = cur.fetchone()[0]
print(f"Inserted user with ID: {user_id}")

# Query data
cur.execute("SELECT id, name, email FROM users")
rows = cur.fetchall()

for row in rows:
    print(row)

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()
