
from email.message import EmailMessage

from app2 import password
import ssl
import smtplib


email_sender = " shashankprof44@gmail.com"
email_password = password
email_reciever = r"shashank944533@gmail.com"

subject ="Dont loose your hope"
body = """
When you study keep motivated 
"""


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body) 


context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
