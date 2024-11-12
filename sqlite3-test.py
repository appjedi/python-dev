#!/usr/bin/python

import sqlite3
import datetime
conn = sqlite3.connect('data.db')

print ("Opened database successfully");

def getUsers():
    cursor = conn.execute("SELECT * from users")
    for row in cursor:
        print(row)

def insertUser():
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input ("Enter email: ")
    dt = datetime.datetime.now()
    cursor = conn.execute("INSERT INTO users (username, password,email,created,role_id,status) VALUES (?, ?,?,?,1,1)", (username, password, email,dt))
    conn.commit()
    print("User inserted successfully")

def updateUser():
    username = input("Enter username: ")
    password = input("Enter password: ")
    cursor = conn.execute("UPDATE users SET password=? WHERE username=? ", (password,username))
    conn.commit()
    print("User inserted successfully")
#insertUser()
#updateUser()
getUsers()
conn.close()