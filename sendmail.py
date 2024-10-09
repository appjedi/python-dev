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
    user="timlinator@gmail.com"
    pw="nwhx npae szit giqk"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, pw)

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

sendToUsers()