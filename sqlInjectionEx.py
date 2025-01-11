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

    conn.commit()



if __name__ == "__main__":
    authUser()
