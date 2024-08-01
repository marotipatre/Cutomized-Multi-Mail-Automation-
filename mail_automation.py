import smtplib 
import os
from dotenv import load_dotenv
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

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


 



text = '''<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exclusive Invitation to Algorand Road to Impact'24 Pune</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            color: #333;
            line-height: 1.6;
        }}
        .container {{
            max-width: 600px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
        }}
        .header {{
            text-align: center;
            margin-bottom: 20px;
        }}
        .header h1 {{
            color: #0062CC;
        }}
        .highlight {{
            color: #0062CC;
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            color: #fff; /* Change text color to white */
            background-color: #0062CC; /* Ensure background color is blue */
            text-decoration: none; /* Remove underline */
            border-radius: 5px;
            font-weight: bold; /* Make the text bold */
        }}
        .footer {{
            text-align: left;
            margin-top: 20px;
        }}
        .button a {{
            color: inherit; /* Inherit color from parent */
            text-decoration: none; /* Remove underline */
        }}
        .button:hover {{
        background-color: #0056b3;
                }}
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>🚀 Exciting News, Web3 Enthusiasts and Founders! 🚀</h1>
            <img src="cid:image1" alt="Event Banner" style="width: 100%; height: auto; border-radius: 10px; margin-top: 10px;">
        </header>
        
        <section>
            <p>Dear <strong>{name}</strong>,</p>
            <p>We hope this message finds you well. As a valued member of our previous Algo Meet in Pune, we are delighted to extend an exclusive invitation to you for the <strong>Algorand Road to Impact'24 Pune</strong> event, happening on <strong>6th August 2024</strong> at the prestigious Redbricks Offices, Pavallion Mall, Pune.</p>
            
            <p class="highlight"><strong>Event Highlights:</strong></p>
            <ul>
                <li>Network with Industry Leaders and like-minded Web3 enthusiasts</li>
                <li>Pitch your groundbreaking ideas to top investors</li>
                <li>Engage in hands-on workshops designed to elevate your skills</li>
                <li>Experience exciting demos and witness the latest innovations</li>
                <li>Collaborate with top developers and industry experts</li>
            </ul>
            
            <p>We believe your presence will greatly enrich the event, and we're confident you'll gain invaluable insights and connections. This is a unique opportunity to propel your projects forward and potentially showcase your product at the <strong>Algorand Bharat Impact Summit'24</strong>!</p>
            
            <p class="highlight"><strong>Next Steps:</strong></p>
            <p>Please review the detailed agenda and further information by accessing the <a href="https://docs.google.com/document/d/1iQ44ipd0I-A83m2n5-uspsSWfCjQXvxwv2vJCBJOFxs/edit?usp=sharing" style="color: #0062CC;">Google Doc</a>. To secure your spot, we kindly ask you to register at the link below:</p>
            <p style="text-align: center;"><button class = "button"><a href="https://lu.ma/74s69k55">Register Now</a></button></p>
            <p style="color: red;"><strong>Kindly note that attendance is by approval only, so please ensure you complete the registration soon.</strong></p>

            <p>For more details and to learn more about the event, visit our main registration page: <a href="https://algobharat.in/road2impact/" style="color: #0062CC;">Algorand Road to Impact'24 Pune</a>.</p>
        </section>
        
        <footer class="footer">
            <p>We are excited about the opportunity to connect with you again and witness the incredible progress you've made since our last meet.</p>
            <p>Best regards,<br>Maroti and the Algorand Road to Impact Team</p>
        </footer>
    </div>
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
        
       # Attach the image
        with open("RTI.jpeg", 'rb') as img_file:
            img = MIMEImage(img_file.read())
            img.add_header('Content-ID', '<image1>')
            message.attach(img) 

        my_server.sendmail(
                from_addr= my_email,
                to_addrs= email,
                msg=message.as_string()
            )
        print(f"Email sent to {name} at {email}")

my_server.quit()