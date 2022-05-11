# Python-Code
import smtplib
from email.message import EmailMessage

email =EmailMessage()
email["from"] = "Python Brothers"
email["to"] = "srabonemam4@gmail.com"
email["subject"] = "You got hala from your GF"

email.set_content("Hi Kaga! What is your GF name?")

with smtplib.SMTP(host = "smtp.gmail.com", port=597) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login("Pybrothers213@gmail.com","python@52266")

  print("Email sent")
