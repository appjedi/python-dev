# https://www.youtube.com/watch?v=g_j6ILT-X0k
# https://myaccount.google.com/u/4/apppasswords
#user="appjedi.net@gmail.com"
#pw="dekxwtulmsryovls"
user="timlinator@gmail.com"
pw="nwhx npae szit giqk"
subject="Hello, world!"
body="This is a test email from Python."

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(user, pw)

message = f"Subject: {subject}\n\n{body}"

server.sendmail(user, 'timlinr@outlook.com', message)
server.quit()
