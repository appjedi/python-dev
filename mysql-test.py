
# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Jedi2024"
)


def get_users():
    cursorObject = dataBase.cursor()
    query = "SELECT * FROM users"
    cursorObject.execute(query)

    myresult = cursorObject.fetchall()

    for x in myresult:
        print(x)
    dataBase.close()


# disconnecting from server

get_users()
