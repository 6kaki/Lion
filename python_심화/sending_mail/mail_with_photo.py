"""
메일에 사진 첨부하기
    
    - codelion.png를 파이썬 코드로 읽어와야한다.
        - open()
            - rb : read binary
            - wb : write binary
            - ab : append binary
            - binary -> 컴퓨터가 이미지를 이해할 수 있도록
                - jpg, exe, png, mp4, mov 등
"""
import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()
message.set_content("이야 신기하다.")
message['Subject'] = "메일 제목"
message['From'] = "###"
message['To'] = "###"

#파일 읽어오기
#img = open('codelion.png','rb')
#파일 출력
#print(img.read())
# 이상한 문자들이 터미널에 출력
# binary 파일

#close() 없이 자동으로 닫기
with open('codelion.png','rb') as image:
    image_file = image.read()

"""
메일에 이미지 첨부하기
    - 메일 내용 안에 일반적인 텍스트가 아니라 다른 형태를 첨부할 때
    - add_attachment()
    - MIME mixed type
        - 이전 text는 plain type
    1. image
    2. maintype
        - 첨부한 파일의 유형 (image, video)
    3. subtype
        - 확장자 (.png)
"""

"""
"png"로만 적으면 매번 수정해줘야한다.  jpg 등
확장자가 변경되어도 알아서 확장자를 파악해서 변경해주는 작업

    - import imghdr
"""

import imghdr

# 어떤 확장자인지 알아낸다.
image_type = imghdr.what('codelion',image_file)
# ('파일이름',읽어온 이미지)
print(image_type)
file_name = 'codelion.'+image_type
print(file_name)
#png
#이미지의 확장자가 변경되어도 동적으로 받아올수있다.

message.add_attachment(image_file, maintype='image',subtype=image_type,filename=file_name)

# "png"로만 적으면 매번 수정해줘야한다.  jpg 등
# 확장자가 변경되어도 알아서 확장자를 파악해서 변경해주는 작업

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("###", "###")
smtp.send_message(message)
smtp.quit()
