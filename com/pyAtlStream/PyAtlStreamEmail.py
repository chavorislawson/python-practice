# Automated emailer
import smtplib
import ssl
from email.mime.text import MIMEText  # add html to library?

# want to send a backup email because you might not be able to use html
from email.mime.multipart import MIMEMultipart

import csv

# with open("somefile.csv") as file:
#     reader = csv.reader(file)
#     next(reader)
#     for name,

sender_email = "" #an email address, I used gmail
receiver_email = ""# same email as above
password = input("Type password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "some testing now"
message["From"] = sender_email
message["To"] = receiver_email

# Message
text = """\
    Wasup,
    How are you doing during this time period?
    Stay indoors, corona be murdering people.
    """
html = """\
        <html>
            <body>
                <p>Hello my good compatriot<br>
                you good?
                yeah?
                ok
                <img src="https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.freelogodesign.org%2FContent%2Fimg%2Flogo-samples%2Fflooop.png&imgrefurl=https%3A%2F%2Fwww.freelogodesign.org%2F&tbnid=fmTUUdU0pbnbuM&vet=12ahUKEwi9i9X0mILpAhWFVKwKHUSXDL8QMygHegUIARCoAg..i&docid=1FqkMM1hJtCa2M&w=500&h=500&q=logo&ved=2ahUKEwi9i9X0mILpAhWFVKwKHUSXDL8QMygHegUIARCoAg">
                a nice image from google
                </p>
            </body>
        </html>
    """
#reference them as object to multipart
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()

# you need to turn on access in the gmail app for this to work

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )


#def spamemail(i):
    # put all that in the function
    # pass i to sender and receiver
    # use a list or sqlserver to spam emails




# make a discord bot to spam people
# create a discord server