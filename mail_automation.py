import smtplib 
import os
from dotenv import load_dotenv
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

my_email = os.getenv('Email')
password_key= os.getenv('Password')


# SMTP Server and port no for GMAIL.com
gmail_server= "smtp.gmail.com"
gmail_port= 587
 
# Starting connection
my_server = smtplib.SMTP(gmail_server, gmail_port)
my_server.ehlo()
my_server.starttls()
      
# Login with your email and password
try:
    my_server.login(my_email, password_key)
    print("Login successful")
except smtplib.SMTPAuthenticationError as e:
    print(f"Failed to login: {e}")


 



text = '''<html>
<body>
<p>Hello {name},</p>
<p>This is a test email.</p>
<p>Here is the link: <a href="https://algobharat.in/road2impact/">Click here</a></p>
</body>
</html>'''

# Reading the csv file

with open ("Book3.csv") as csv_file: 
    book3 = csv.reader(csv_file)
    next(book3) # Skip header row
    for name,email in book3:
        
        email_text=text.format(name=name)
        message = MIMEMultipart()
        message['From'] = my_email
        message['To'] = email
        message['Subject'] = "Test Email"
        message.attach(MIMEText(email_text, 'html'))
        
        

        my_server.sendmail(
                from_addr= my_email,
                to_addrs= email,
                msg=message.as_string()
            )
        print(f"Email sent to {name} at {email}")

my_server.quit()