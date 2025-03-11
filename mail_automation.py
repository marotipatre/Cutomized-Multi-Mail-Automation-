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
    <title>Congratulations: You're Advancing to AlgoBharat Hack-Series Phase 2!</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            color: #333;
            line-height: 1.6;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }}
        .container {{
            max-width: 600px;
            margin: auto;
            background-color: #ffffff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 25px;
            border-bottom: 3px solid #0062CC;
            padding-bottom: 15px;
        }}
        .header h1 {{
            color: #0062CC;
            margin-top: 10px;
            font-size: 24px;
        }}
        .header img {{
            width: 100%;
            border-radius: 10px;
            margin-bottom: 15px;
        }}
        .highlight {{
            color: #0062CC;
            font-weight: bold;
        }}
        .section {{
            margin-bottom: 20px;
            padding: 15px;
            background-color: #f5f9ff;
            border-radius: 10px;
            text-align: justify;
        }}
        .section h2 {{
            color: #0062CC;
            margin-top: 0;
            border-bottom: 1px solid #cce0ff;
            padding-bottom: 8px;
            font-size: 18px;
        }}
        .priority-section {{
            background-color: #e6f2ff;
            border: 2px solid #0062CC;
            box-shadow: 0 3px 10px rgba(0,98,204,0.2);
        }}
        .button {{
            display: inline-block;
            padding: 12px 25px;
            color: #fff;
            background-color: #0062CC;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            text-align: center;
            margin: 15px 0;
            transition: all 0.3s ease;
        }}
        .button:hover {{
            background-color: #0056b3;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .telegram-button {{
            background-color: #26A5E4;
            font-size: 16px;
            padding: 14px 28px;
        }}
        .telegram-button:hover {{
            background-color: #0088cc;
        }}
        .footer {{
            text-align: justify;
            margin-top: 30px;
            padding-top: 15px;
            border-top: 1px solid #eee;
            font-size: 14px;
        }}
        .timeline {{
            margin: 20px 0;
            padding: 0;
        }}
        .timeline li {{
            padding: 10px 0 10px 30px;
            position: relative;
            list-style-type: none;
            text-align: left;
        }}
        .timeline li:before {{
            content: '●';
            position: absolute;
            left: 0;
            color: #0062CC;
            font-size: 18px;
        }}
        .personal-note {{
            font-style: italic;
            border-left: 3px solid #0062CC;
            padding-left: 15px;
            margin: 20px 0;
            text-align: justify;
        }}
        .action-required {{
            background-color: #ffe6e6;
            border-left: 4px solid #ff5252;
            padding: 10px 15px;
            margin: 15px 0;
        }}
        .mandatory-notice {{
            color: #ff3333;
            font-weight: bold;
            font-size: 15px;
            margin-top: 10px;
        }}
        p, li {{
            text-align: justify;
        }}
        .center-content {{
            text-align: center;
        }}
        .starred-note {{
            font-style: italic;
            color: #0062CC;
            margin: 15px 0;
            padding: 10px;
            border: 1px dashed #0062CC;
            background-color: #f0f7ff;
            border-radius: 5px;
        }}
        .social-links {{
            display: flex;
            justify-content: center;
            margin: 15px 0;
            gap: 20px;
        }}
        .social-link {{
            display: inline-flex;
            align-items: center;
            padding: 8px 15px;
            border-radius: 5px;
            font-weight: bold;
            color: white;
            text-decoration: none;
            transition: all 0.3s ease;
        }}
        .social-link:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .telegram-link {{
            background-color: #26A5E4;
        }}
        .telegram-link:hover {{
            background-color: #0088cc;
        }}
        .twitter-link {{
            background-color: #1DA1F2;
        }}
        .twitter-link:hover {{
            background-color: #0d8ddb;
        }}
        .linkedin-link {{
            background-color: #0077B5;
        }}
        .linkedin-link:hover {{
            background-color: #00669c;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>🎉 CONGRATULATIONS, {name}! YOU'RE ADVANCING TO PHASE 1! 🎉</h1>
        </header>
        
        <section>
            <p>Dear <strong>{name}</strong>,</p>
            
            <p>I'm thrilled to inform you that based on your impressive Expression of Interest, you've been <span class="highlight">shortlisted for Phase 1</span> of the AlgoBharat Hack-Series in the <span class="highlight">"Bring Your Own Project"</span> track!</p>
            
            <div class="personal-note">
                <p>As the lead for the "Bring Your Own Project" track, I'm personally excited about your project idea and am looking forward to working with you to refine and develop it further. I'll be your dedicated guide throughout this journey!</p>
            </div>
            
            <div class="section priority-section">
                <h2>🤝 JOIN OUR COMMUNITY - MANDATORY</h2>
                <p>I've created a dedicated Telegram group for all "Bring Your Own Project" track participants. Joining this group is <strong>MANDATORY</strong> as it will be our primary communication channel throughout the hackathon.</p>
                <p>In this group, we will:</p>
                <ul>
                    <li>Provide ideation support and technical guidance</li>
                    <li>Connect you with potential teammates</li>
                    <li>Answer your questions in real-time</li>
                    <li>Share resources and inspiration</li>
                    <li>Make important announcements about deadlines and events</li>
                </ul>
                
                <div class="center-content">
                    <a href="https://t.me/AlgoBharatBYOP" class="button telegram-button">Join Telegram Group Now</a>
                </div>
                <p class="mandatory-notice center-content">⚠️ All further communications will happen through this group - joining is required to proceed! ⚠️</p>
            </div>
            
            <div class="section">
                <h2>🚀 WHAT HAPPENS IN PHASE 2?</h2>
                <p>Now is the time to transform your initial concept into a detailed project proposal. This is where your vision starts taking concrete shape!</p>
                
                <div class="action-required">
                    <p><strong>ACTION REQUIRED:</strong> Submit your detailed project idea by <strong>March 31, 2025</strong></p>
                </div>
                
                <p>Your submission should include:</p>
                <ul>
                    <li>Comprehensive project/module description</li>
                    <li>Problem statement and proposed solution</li>
                    <li>Technical architecture overview</li>
                    <li>Implementation plan and timeline</li>
                    <li>Expected impact and outcomes</li>
                </ul>

                 <div class="starred-note">
                    <p>* I strongly encourage you to join our Telegram group to refine and polish your ideas before submission. As your track leader, I'm here to provide personalized guidance to help strengthen your proposal. Don't hesitate to reach out for assistance - that's what I'm here for! *</p>
                </div>
                
                <div class="center-content">
                    <a href="https://docs.google.com/forms/d/e/1FAIpQLSdPbAzcotEXqU82h5kFMu6eNtTVlUA3wB2A0hmI8j3iTk_W6g/viewform" class="button">Submit Your Detailed Proposal</a>
                </div>
            </div>
            
            <div class="section">
                <h2>📅 KEY DATES</h2>
                <ul class="timeline">
                    <li><strong>March 15, 2025:</strong> Phase 2 Kickoff Webinar</li>
                    <li><strong>March 21, 2025:</strong> Project Description Form submission deadline</li>
                </ul>
            </div>
            
            <div class="section">
                <h2>🌟 HOW I CAN HELP YOU</h2>
                <p>As your track lead, I'm committed to helping you succeed. I can provide:</p>
                <ul>
                    <li>Personalized feedback on your project idea</li>
                    <li>Technical guidance and resources</li>
                    <li>Connections to relevant industry experts</li>
                    <li>Regular office hours for direct consultations</li>
                    <li>Support in refining your value proposition</li>
                </ul>
                <p>Don't hesitate to reach out to me directly with any questions!</p>
                 <div class="social-links">
                    <a href="https://t.me/maroti_ps" class="social-link telegram-link">
                        📱 Telegram
                    </a>
                    <a href="https://twitter.com/maroti_ps" class="social-link twitter-link">
                        🐦 Twitter
                    </a>
                    <a href="https://linkedin.com/in/maroti-patre" class="social-link linkedin-link">
                        👔 LinkedIn
                    </a>
                </div>
            </div>
        </section>
        
        <footer class="footer">
            <p>I'm looking forward to seeing your innovative ideas come to life on the Algorand blockchain!</p>
            <p>Best regards,<br><strong>Maroti Patre</strong><br>Track Lead - Bring Your Own Project<br>AlgoBharat Hack-Series</p>
            <p style="font-size: 12px; color: #999; margin-top: 20px;">If you believe you received this email in error, please contact us at support@algobharat.in</p>
        </footer>
    </div>
</body>
</html>'''

# Reading the csv file

with open ("Book3.csv") as csv_file: 
    book3 = csv.reader(csv_file)
    next(book3) # Skip header row
    for name,email in book3:
        
        # Extract just the first name (everything before the first space)
        first_name = name.split()[0]
        
        # Use first_name in the email template instead of the full name
        email_text = text.format(name=first_name)

        message = MIMEMultipart()
        message['From'] = my_email
        message['To'] = email
        message['Subject'] = "🎉 CONGRATULATIONS! You hav Advanced to AlgoBharat Phase 1 BYOP track - Next Steps Inside"
        message.attach(MIMEText(email_text, 'html'))
        
        my_server.sendmail(
                from_addr= my_email,
                to_addrs= email,
                msg=message.as_string()
            )
        print(f"Email sent to {name} at {email}")

my_server.quit()