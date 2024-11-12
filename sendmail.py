# https://www.youtube.com/watch?v=g_j6ILT-X0k
# https://www.youtube.com/watch?v=OLrC4J2-pvk
# https://myaccount.google.com/u/4/apppasswords
# https://github.com/Sven-Bo/automate-sending-emails-using-python/tree/master
#user="appjedi.net@gmail.com"
#pw="dekxwtulmsryovls"
import smtplib
import sqlite3

conn = sqlite3.connect('data.db')

def send_email(to, subject, body):
    user="appdojo.net@gmail.com"
    pw="nwhx npae szit giqk"
    appDojoPW="uovy zaeu yxyu sbps"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, appDojoPW)

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail(user, to, message)
    server.quit()

def sendToUsers():
    subject=input("Subject: ")
    body =input ("Message:")
    cursor = conn.execute("SELECT * from users")
    for row in cursor:
        print (f"Sending email to {row[5]}")
        send_email(row[5], subject, body)
def getUsers():
    users=[]
    cursor = conn.execute("SELECT * from users")
    for row in cursor:
        #print (row)
        user ={'id':row[0], 'username':row[1],'email':row[5], 'roleId':row[3], 'status':row[4], 'created':row[6]}
        users.append(user)

    return users

print(getUsers())     
#sendToUsers()