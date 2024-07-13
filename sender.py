import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import locale

smtp_server = 'smtp.daum.net'
smtp_port = 465


sender_email = 'ferdavs@daum.net'



recipient_email = 'ferdavs@naver.com'  # Change this to the recipient's email address
# Set the locale to Korean
locale.setlocale(locale.LC_TIME, 'ko_KR.UTF-8')

# Get today's date and format it in Korean
today = datetime.now()
formatted_date = today.strftime("%Y년 %m월 %d일") 

# Append "daily report" to the subject
subject = f"{formatted_date} 일일 보고서" 
body = input("Enter the body of the text -__-:")
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server
try:
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(sender_email, sender_password)
except smtplib.SMTPException as e:
    print(f"Error: Unable to connect and log in to the SMTP server. {e}")
    exit()

# Send the email
try:
    server.sendmail(sender_email, recipient_email, message.as_string())
    print("Email sent successfully.")
except smtplib.SMTPException as e:
    print(f"Error: Unable to send the email. {e}")
finally:
    server.quit()
