import pymysql

def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="Jedi2023",
        db='training',
    )

    return  conn

def getAllUsers():
    conn = mysqlconnect()
    cur=conn.cursor()
    cur.execute("select * from users")
    output = cur.fetchall()
    #print(output)
    for row in output:
        print(row)
    # To close the connection
    conn.close()

def getUser():
    conn = mysqlconnect()
    cur=conn.cursor()
    username = input("Enter username: ")

    cur.execute("select * from users where username=%s", (username,))
    output = cur.fetchall()
    #print(output)
    for row in output:
        print(row)
    # To close the connection
    conn.close()
def authUser():
    conn = mysqlconnect()
    cur=conn.cursor()
    username = input("Enter username: ")
    password = input("Enter password: ")
    prep = "select * from users where username=%s AND password=%s"
    sp = "call usp_user_auth(%s,%s)"
    cur.execute(sp, (username,password))
    output = cur.fetchall()
    #print(output)
    for row in output:
        print(row)
    # To close the connection
    conn.close()
def hackUser():
    conn = mysqlconnect()
    cur=conn.cursor()
    username = input("Enter username: ")
    password = input("Enter password: ")
    sql= "select * from users where username='{0}' AND password='{1}'".format(username,password)
    print(sql)
    cur.execute(sql)
    output = cur.fetchall()
    #print(output)
    for row in output:
        print(row)
    # To close the connection
    conn.close()
# Driver Code
def addUser():
    username=input('Username: ')
    password=input('Password: ')
    conn = mysqlconnect()
    cur=conn.cursor()
    sql = "INSERT INTO `users` (`username`, `password`, role_id, status, created) VALUES (%s, %s,1,1,SYSDATE())"
    cur.execute(sql, (username, password))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    conn.commit()

def changeRole():
    username=input('Username: ')
    newRole=input('New Role: ')
    conn = mysqlconnect()
    cur=conn.cursor()
    sql = "UPDATE `users` SET role_id=%s WHERE username=%s"
    cur.execute(sql, (newRole, username))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    conn.commit()

def deleteUser():
    username=input('Username: ')
    conn = mysqlconnect()
    cur=conn.cursor()
    sql = "DELETE FROM `users` WHERE username=%s"
    cur.execute(sql, (username,))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    conn.commit()

if __name__ == "__main__":
    getAllUsers()
