import pymysql

# Connect to the database
connection = pymysql.connect(
        host='localhost',
        user='root',
        password="",
        db='test',
    )
def insertUser():
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            username=input('Username: ')
            password=input('Password: ')
            sql = "INSERT INTO `users` (`username`, `password`, role_id, status, created) VALUES (%s, %s,1,1,SYSDATE())"
            cursor.execute(sql, (username, password))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
def getUser():
        username=input("username")
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `userid`, `password` FROM `users` WHERE `username`=%s"
            cursor.execute(sql, (username,))
            result = cursor.fetchone()
            print(result)
def getUsers():
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `users`"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(row)            
getUsers()
#insertUser()