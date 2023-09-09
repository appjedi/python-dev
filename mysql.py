#!/usr/bin/python

import MySQLdb

# Open database connection

def getConn():
#db = MySQLdb.connect(host="localhost",user="root",password="maria1",database="test")
    db = MySQLdb.connect(host="localhost", user="devuser",
                     password="Jedi2023", database="dev")
    return db
def getLogs():
    # prepare a cursor object using cursor() method
    db=getConn()
    cursor = db.cursor()
#sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
#val = ("John", "Highway21")
#cursor.execute(sql, val)
# execute SQL query using execute() method.
    cursor.execute("SELECT message FROM logger")
    results = cursor.fetchall()
    for row in results:
        print(row[0])
# Fetch a single row using fetchone() method.

# disconnect from server
    db.close()
def getUsers():
    db=getConn()
    cursor = db.cursor()
#sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
#val = ("John", "Highway21")
#cursor.execute(sql, val)
# execute SQL query using execute() method.
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for row in results:
        print(row[1])

def log(msg, src):

    insert="INSERT INTO `dev`.`logger`(`message`,`source`,`log_stamp`)VALUES(%s,%s, SYSDATE())"
    values=[msg,src]
    db=getConn()
    cursor = db.cursor()
    cursor.execute(insert,values)
    db.commit()
    db.close()

log("Hello from Ubunto", 2)
getLogs()