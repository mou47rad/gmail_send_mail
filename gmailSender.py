import smtplib, ssl
from email.mime.text import MIMEText


sender = 'mail_sender@gmail.com'
receivers = 'mail_receiver@gmail.com'
body_of_email = 'Text to be displayed in the email'

msg = MIMEText(body_of_email, 'html')
msg['Subject'] = 'test messge'
msg['From'] = sender
msg['To'] = 'your name'

s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = sender, password = 'your_passworad')
s.sendmail(sender, receivers, msg.as_string())
s.quit()