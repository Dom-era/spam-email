import smtplib
from email.mime.text import MIMEText

# Gmail SMTP Server Setup
smtp_server = 'smtp.gmail.com'
port = 587
email = 'hellenmwangi@zetech.ac.ke'
app_password = 'yzeuhnjtoacilubq'  # Newly generated app password

# Email Content
msg = MIMEText('This is a test email')
msg['Subject'] = 'Test Email'
msg['From'] = email
msg['To'] = 'fredrick.ochieng@zetech.ac.ke'

# Sending the Email
try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  
    server.starttls()  # Upgrade the connection to TLS
    server.ehlo()  
    server.login(email, app_password)  # Login with app-specific password
    server.sendmail(email, 'fredrick.ochieng@zetech.ac.ke', msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email. Error: {e}")
