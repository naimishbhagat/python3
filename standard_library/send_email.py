from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())
# template.substitute()

message = MIMEMultipart()
message["from"] = "Naimish Bhagat"
message["to"] = "naimish.bhagat.nbw@gmail.com"
message["subject"] = "This is a test"
body = template.substitute({"name": "Naimish"})
message.attach(MIMEText(body, "html"))
# message.attach(MIMEImage(Path("mosh.png").read_bytes()))
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("naimish.bhagat.nbw@gmail.com", "Be4co021")
    smtp.send_message(message)
    print("sent")
