"""
BeautifulSoup
- 다양한 칸막이로 되어있어서 html code를 잘 정리해준다.
    print(response.text)
    print(BeautifulSoup(response.text,'html.parser'))
    - 둘이 다른점?
        - type
            - str
            - bs4.BeautifulSoup
"""

import requests
# import BeautifulSoup # 모듈을 찾을 수 없는 error가 뜬다.
from bs4 import BeautifulSoup # 모듈이름은 bs4이다. BeautifulSoup은 기능의 이름이다.

url = "http://www.daum.net/"
response = requests.get(url)
print(type(response.text)) #<class 'str'>
#필요한 결과값만 뽑아내는 작업
#실시간 검색어만 빼오기

# BeautifulSoup 통에 넣어서 원하는 부분만 빼올 수 있다.
print(type(BeautifulSoup(response.text,'html.parser'))) #<class 'bs4.BeautifulSoup'>

