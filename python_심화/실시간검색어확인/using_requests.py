"""
키트에서
자동차 조립 기계를 꺼내고
자동차를 조립해줘
-> 자동자 완성

requests 모듈에서
get함수를 꺼내서
요청을 보내줘
-> 응답값을 받는다. -> return 응답값

- requests.get(url)
 - get 요청을 보내는 기능
 - 요청에는 put, post, delete 등 다양하게 있다.
 - 요청이란?
    - 요청과 응답은 쌍으로 다닌다.
    - 요청(client) : url의 정보
    - 응답(server) : 홈페이지의 html정보를 return
 - requests.get(url,params=None, **kwargs)
    - params : 함수에게 필요한 재료
 - return : requests.response -> 서버의 응답값
 - html code 받아오기 : response.text
    - url : https://www.daum.net
    - content : html code
    - encoding : ISO-8859-1
    - headers : {'Date': 'Tue, 03 May 2022 07:44:58 GMT',
        'Content-Type': 'text/html', 'Transfer-Encoding': 'chunked',
        'Connection': 'keep-alive', 'Vary': 'Accept-Encoding, Origin, Accept-Encoding',
        'Access-Control-Allow-Origin': '*',
        'X-WCSS': 'dC1jb21tb24wMS1id2NhY2hlMjc6MDpjaHR0cDoxNg==',
        'Cache-Control': 'no-cache, no-store', 'Pragma': 'no-cache', '
        Strict-Transport-Security': 'max-age=15724800', 'Content-Encoding': 'gzip'}
    - json : <bound method Response.json of <Response [200]>>
    - links : {}
    - ok : True
    - status_code : 200
"""
import requests #모듈 (키트)

#print(requests.get) #<function get at 0x7fb6be907940> get이라는 이름의 함수입니다.
url = 'http://www.daum.net' #서버 주소
#print(requests.get(url)) # 요청을 보낸다. # <Response [200]> [200] : 성공을 의미
response = requests.get(url)
# print(response) # <Response [200]>
# print(response.text) # 텍스트를 꺼내와줘 # html code를 가져온다.
print(response.encoding)


