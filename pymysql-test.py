import pymysql

# Connect to the database
connection = pymysql.connect(
        host='localhost',
        user='root',
        password="Jedi2023",
        db='dev',
    )

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

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `user_id`, `password` FROM `users` WHERE `username`=%s"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()
        print(result)
