import pymysql


def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="Jedi2023",
        db='dev',
    )

    cur = conn.cursor()
    cur.execute("select * from users")
    output = cur.fetchall()
    print(output)

    # To close the connection
    conn.close()


# Driver Code
if __name__ == "__main__":
    mysqlconnect()
