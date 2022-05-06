"""
API key 발급받기

https://home.openweathermap.org/users/sign_up

도시별 날씨 정보 받아오기
"""
#------------------------------------------------------#
"""
API 알아보기
    - 응용프로그램 프로그래밍 인터페이스
    - interface
        - 키보드, 마우스 (사람과 컴퓨터를 이어주는 interface)
        - 휴대폰 (사람과 사람을 이어주는 interface)
        - API (client컴퓨터와 server 컴퓨터를 이어주는 interface)
            - html은 서버에 직접 접근한 것
            - 데이터를 원활하게 주고받기 위해서 API가 존재
            - client와 server 중간에서 데이터가 잘 오고갈수있도록 약속
    - 날씨정보를 출력하는 프로그램
        - 1분 1초 단위로 변하는 날씨 정보
        - 기상청 사이트에서 날씨를 크롤링할 수 있다.
            - 하지만 크롤링은 한정적인 데이터만 가져올수있다.
            - 직접표기된 데이터가 아니라면 가져올수없다.
        - API를 활용
    - Openweathermap API를 이용
        - 비용없이 사용가능한 API
            - openAPI
"""
#------------------------------------------------------#
"""
API key 알아보기
- 내가 만든 API를 누가 사용하는지 알려고
- key를 발급받아 사용한다. (방명록)
    - 철수, 영희
    - 일종의 문자열로 이루어져있다.
"""
#------------------------------------------------------#
"""
API 링크 만들기

- API doc
    - 사용방법 설명서
    - 지역이름으로 날씨를 받아오는 API
        - https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
    - API를 call한다.
        - server에 요청한다.

"""
#------------------------------------------------------#
# city = 'Seoul'
# apikey = '6f5b0c78c06671837ff7ba4d369fe932'
# #parameter 조건 
# #city와 APIkey
# api=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}'
#변수의 내용만 바꿔주면 링크가 바뀐다.
# city='Newyork'
#print(api)
#------------------------------------------------------#
"""
api => api server의 주소를 완성한 것이다.
server 주소의 의미
    - ?
        - 물음표를 기준으로 공통 url
        - 물음표 뒷쪽은 파라미터
            - ?q={}&appid={} 

요청 보내기
    - import requests
"""
#------------------------------------------------------#
# import requests

# response = requests.get(api)
# print(response.text)
# print(type(response.text))
#str type -> json 모듈을 사용
"""
{
    "coord":{"lon":126.9778,"lat":37.5683},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"stations",
    "main":
    {
        "temp":290.04,
        "feels_like":290,
        "temp_min":288.84,
        "temp_max":290.81,
        "pressure":1016,
        "humidity":85
    },
    "visibility":7000,
    "wind":{"speed":2.57,"deg":240},
    "clouds":{"all":75},
    "dt":1651846521,
    "sys":{"type":1,"id":8105,"country":"KR","sunrise":1651782708,"sunset":1651832737},
    "timezone":32400,
    "id":1835848,
    "name":"Seoul",
    "cod":200
}
"""
#------------------------------------------------------#
"""
가공하기

- str type이지만 json 형식으로 적혀있다.
- 데이터를 주고 받을 때 사용하는 포멧
- dict형식과 비슷하지만 "문자열"

json module을 사용하기
"""
# import json

# data = json.loads(response.text)
#str타입을 json 형식으로 바꿔주기

#print(type(data))
#<class 'dict'>
#------------------------------------------------------#
"""
필요한 데이터만 나열하기

언어 및 단위 변환
lang = 'kr'
units='metric'
api=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}'

"""
import requests
import json
from datetime import datetime

city = 'Seoul'
apikey = '6f5b0c78c06671837ff7ba4d369fe932'
lang='kr'
units='metric'
#parameter 조건 
#city와 APIkey
api=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units={units}'
response = requests.get(api)
data = json.loads(response.text)


print(datetime.today().strftime("%Y년 %m월 %d일 %H시 %M분"))
print(data["name"]+'의 날씨입니다.')
#Seoul의 날씨입니다.
print("날씨는 "+data["weather"][0]["description"]+"입니다.")
#Clouds
C_temp = data["main"]["temp"]
print("현재온도는 "+str(C_temp)+"입니다.")
#현재온도는 289.9입니다.
feels_temp = data["main"]["feels_like"]
print("하지만 체감온도는 "+str(feels_temp)+"입니다.")
#하지만 체감온도는 289.85입니다.

#최저 기온 
print("최저 기온은 "+str(data["main"]["temp_min"]))
#최고 기온 
print("최고 기온은 "+str(data["main"]["temp_max"]))
#습도
print("습도는 "+str(data["main"]["humidity"]))
#기압
print("기압은 "+str(data["main"]["pressure"]))
#풍향
print("풍향은 "+str(data["wind"]["deg"]))
# 풍속
print("풍속은 "+str(data["wind"]["speed"])+"입니다.")
#------------------------------------------------------#
