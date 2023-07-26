#!/usr/bin/python

import MySQLdb

# Open database connection

#db = MySQLdb.connect(host="localhost",user="root",password="maria1",database="test")
db = MySQLdb.connect(host="appdojo.net", user="appjedin_sensei",
                     password="Sensei2022!", database="appjedin_training")

# prepare a cursor object using cursor() method
cursor = db.cursor()
#sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
#val = ("John", "Highway21")
#cursor.execute(sql, val)
# execute SQL query using execute() method.
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()
for row in results:
    print(row[1])
# Fetch a single row using fetchone() method.

# disconnect from server
db.close()
