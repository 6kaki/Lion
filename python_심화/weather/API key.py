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
city = 'Seoul'
apikey = '6f5b0c78c06671837ff7ba4d369fe932'
#parameter 조건 
#city와 APIkey
api=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}'
#변수의 내용만 바꿔주면 링크가 바뀐다.
# city='Newyork'
print(api)
#------------------------------------------------------#
"""
api => api server의 주소를 완성한 것이다.
"""
#------------------------------------------------------#
"""
"""

