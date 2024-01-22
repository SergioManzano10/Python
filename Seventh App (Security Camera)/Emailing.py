import email
import imghdr
from email.message import EmailMessage
from importlib.resources import contents
import smtplib

password = "razl xzkv ggfz dqbw"
username = "smanzano250800@gmail.com"

def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage() 
    email_message["Subject"] = "New customer showed up!" 
    email_message.set_content("We just see a new customer!") 

    with open(image_path, "rb") as file:
        content = file.read()
    
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, username, email_message.as_string())
    gmail.quit()
    print("send_email function finished")


    if __name__ == "__main__":
        send_email(image_path="images/19.png")