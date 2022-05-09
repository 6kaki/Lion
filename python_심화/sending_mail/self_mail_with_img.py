import smtplib
from email.message import EmailMessage
import imghdr

with open('codelion.png','rb') as image:
    image_file = image.read()

image_type = imghdr.what('codelion',image_file)



message = EmailMessage()
message.set_content("와 신기하다.")
message['To'] = "poijnm66@naver.com"
message['From'] = "juniyook@likelion.org"
message['Subject'] = "img_with_email"
message.add_attachment(image_file,maintype='image',subtype=image_type,filename='codelion.png')

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("juniyook@likelion.org","@ldrmfdl66")
smtp.send_message(message)
smtp.quit()