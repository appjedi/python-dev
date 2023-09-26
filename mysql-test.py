
# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
    host="appdojo.net",
    user="appjedin_sensei",
    passwd="Sensei2022!"
)


def get_users():
    cursorObject = dataBase.cursor()
    query = "SELECT * FROM appjedin_training.users"
    cursorObject.execute(query)

    myresult = cursorObject.fetchall()

    for x in myresult:
        print(x)
    dataBase.close()


# disconnecting from server

get_users()
