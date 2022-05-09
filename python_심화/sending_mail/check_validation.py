"""
email 주소가 맞는지 유효성을 check

    - 정규표현식
        - 문자열에서 나타나는 특정 패턴을 나타내서 대응시킴
            - 이메일에서 나타나는 특정 패턴을 보고 적합한지 확인
            - ^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$
                - ^ : 시작
                - $ : 끝
                - [a-zA-Z0-9.+_-]+
                    - a부터z까지, A부터 Z까지, 0부터 9까지, . , + , _ , - 가 
                    - codelion.example
                - + : 1회 이상 반복된다.
                - @ : 그 뒤에 @가 붙는다.
                    - codelion.example@gmail 
                - \. : .은 원래 모든 문자 
                    - 모든문자가 아니라 실제 점을 원하므로 \를 붙여준다.
                    - codelion.example@gmail.
                - [a-zA-Z]{2,3} : 최소 2, 최대 3번 반복된다.
                    - codelion.example@gmail.com
                    - com 위치가 4,5 글자가 오면 안된다.

"""

import re
import smtplib
from email.message import EmailMessage
import imghdr

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
# print(re.match(reg, message['To'] ))
# print(re.match(reg, message['From'] ))
#(정규표현식, 정규표현식을 적용하고 싶은 문장)
#<re.Match object; span=(0, 18), match='###'>
# 정규표현식에 부합하지 않을경우 : None

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        #bool : 내용이 있으면 True
        #       :내용이 없으면 False
        smtp.send_message(message)
        print("정상적으로 mail이 발송되었습니다.")
    else:
        print("유효한 email 주소가 아닙니다.")

with open('codelion.png','rb') as image:
    image_file = image.read()

img_type = imghdr.what('codelion',image_file)

message = EmailMessage()
message.set_content("와 신기하다.")
message['To'] = '###'
message['From'] = '###'
message['Subject'] = '제목입니다.'
message.add_attachment(image_file,maintype='image',subtype='img_type',filename='codelion.png')

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("###", "###")

sendEmail(message['To'])

smtp.quit()