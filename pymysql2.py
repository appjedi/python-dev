import pymysql

def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="test",
        db='dev',
    )

    cur = conn.cursor()
    cur.execute("select * from users")
    output = cur.fetchall()
    #print(output)
    for row in output:
        print(row[1])
    # To close the connection
    conn.close()

# Driver Code
if __name__ == "__main__":
    mysqlconnect()
