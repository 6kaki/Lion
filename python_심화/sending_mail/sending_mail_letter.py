import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

#MIME로 내용 변환하기
message = EmailMessage()
message.set_content("메일 내용")
messageg['subject'] = "메일 제목"
message['From'] = "내 메일 주소"
message['To'] = "받는 사람 메일 주소"

#SMTP로 서버 연결
smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("내 구글 아이디", "구글 비밀번호")
smtp.send_message(message)
smtp.quit()
#SMTP 연결 끊기