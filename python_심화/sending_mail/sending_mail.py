"""
gmail로 메일 보내기

사전준비 (필수)
    - google 보안 수준 변경
        - https://likelion.notion.site/Google-93ee4cffb5b7481584be4de44ce5bf5e
        - 메일 계정의 외부 접속에 대한 보안 설정
    - google IMAP 상태값 변경
        - https://likelion.notion.site/Google-IMAP-ca417541e62b4f958ff695b8db8c0feb
        - email에 access하기 위해서
        - 실습이 끝나면 다시 돌려놓아도 상관없다.
"""

"""
SMTP 1
    - Simple Mail Transfer Protocol
        - 간단하게 메일을 보내기 위한 약속
        - 평소에 메일을 주고 받을 때도 사용한다.
        - clinet python program (email-client)
            - 메일을 보내면 ("SMTP"를 사용해서)
            - google Email Server에 도착 (a@gmail.com 본인)
            - 메일을 보내고 싶은 다른 사람 (b@gmail.com)
                - a에서 b로 "SMTP"를 사용해서 전송한다.
        - 자신 -> 내 메일 서버 -> b 메일 서버
        - SMTP에 맞춰서 보내주어야한다.

IMAP
    - b -> a 서버로 SMTP를 사용해서 전송
    - a -> clinet로 전송 (IMAP)
    - 허용해야만 다른 이메일 서버에서 보내준 메일, 
        내 메일 서버에 저장되어있는 내용을 clinet로 가져올 수 있다.

나(clinet) -> (SMTP) -> 내 메일 서버 -> (SMTP) -> b 메일 서버
-> (IMAP) -> b clinet

b clinet -> (SMTP) -> b 메일 서버 -> (SMTP) -> a 메일 서버
-> (IMAP) -> a clinet

평소는 server간에 SMTP만 사용하여 메일을 주고 받았다.
            
"""

"""
SMTP 2
    - SMTP 서버를 이용 (smtp.gmail.com동 465번지)
        - Address : stmp.gamil.com
        - Port : 465
            - 주소의 문
        - smtp.gmail.com주소의 465문을 연다
    - smtplib
        - 라이브러리를 활용
            1. SMTP 메일 서버를 연결
                - requests.ger(url)은 응답을 받아오는 것
                - 이와 다르게 "연결"
            2. SMTP 메일 서버에 로그인
            3. SMTP 메일 서버로 메일을 보낸다.
"""
# 1.
import smtplib
#내장 라이브러리

# gmail의 smtp 주소
SMTP_SERVER = "smtp.gmail.com"

# gmail의 SMTP를 이용하려면 "꼭" 465로 지정해야한다.
# gmail에서 지정
SMTP_PORT = 465

#메일 서버 연결
#smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
# (서버주소, Port번호)
# smtp : 연결에 대한 결과값

#print(smtp)
"""
smtplib.SMTPServerDisconnected: Connection unexpectedly closed

connection이 닫혀있다. : 보안 문제
    SSL이라는 것을 필수로 요구한다.
    아무나 접근하지 못하도록하는 암호화 방식
    암호화방식을 포함하는 방법으로 연결해야한다.
"""
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
#SSL 처리 포함한 함수

# print(smtp)
# <smtplib.SMTP_SSL object at 0x7f82dd5a02e0>
# gmail smtp 서버에 접속 성공

"""
2. SMTP 메일 서버에 로그인
    - 객체를 활용해서 로그인
"""
smtp.login('###','###')
# (ID, password)
# (235, b'2.7.0 Accepted')
# If 패스워드가 틀리면 : 오류 출력

"""
3. SMTP 메일 서버로 메일 보내기
    - 
"""
# smtp.send_message()
# # (메일 내용)
# smtp.quit()
# # 끝 !

"""
MIME
    - 전자우편을 위한 인터넷 표준 포멧 (약속)
        - 한글, 사진 등을 이해할수없어서
        - MIME형식으로 "변환"해서 전송 -> SMTP가 이해한다.

    - email.message module
        - 내장 모듈
        - EmailMessage 기능
            - MIME 형태로 변환해준다.
    
    1. email 만들기
        - MIME 형태의 통만들기
    2. email 내용 담기
    3. 발신자, 수신자를 설정
"""
from email.message import EmailMessage

# 1.
message = EmailMessage()

# 2. 본문의 내용을 담는다.
message.set_content("이야 신기하다!!")

# 3.
"""
MIME.Header
    - subject : 제목
    - From : 내 메일 계정
    - To : 메일 받는 사람
"""
message['Subject'] = "똑똑 메일 왔습니다."
message['From'] = "###"
message['To'] = "###"

smtp.send_message(message)
#보내고 싶은 이메일
smtp.quit()
# 끝 !!
