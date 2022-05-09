import re
import smtplib
from email.message import EmailMessage
import imghdr

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465



def sendEmail(emails):
    reg = "^[a-zA-Z0-9+._-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    valid_dict={}
    for key,email in emails.items():
        valid_dict[key]=bool(re.match(reg, email))
    if False in valid_dict.values():
        for k,v in valid_dict.items():
            if v == False:
                print(f"{key} 유효한 email 주소가 아닙니다.")
                
    else:
        smtp.send_message(message)
        print("메일을 성공적으로 보냈습니다.")
    print("="*36)

print("="*36)
From = input('내 메일 주소 : ')
To = input('받는 사람 : ')
Subject = input('메일 제목 : ')
content = input('메일 내용 : ')
print("="*36)

message = EmailMessage()
message.set_content(content)
message['To'] = To
message['From'] = From  
message['Subject'] = Subject

email_dict={
    '내 메일 주소는' : To,
    '받는 사람은' : From
}

with open('codelion.png','rb') as image:
    image_file = image.read()

image_type = imghdr.what('codelion',image_file)

message.add_attachment(image_file,maintype="image",subtype=image_type,filename='codelion.png')

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("#####","####")

sendEmail(email_dict)

smtp.quit()