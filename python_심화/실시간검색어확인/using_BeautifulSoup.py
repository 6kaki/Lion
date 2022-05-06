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
#print(response.text[:500])#<class 'str'>
#필요한 결과값만 뽑아내는 작업
#실시간 검색어만 빼오기

# BeautifulSoup 통에 넣어서 원하는 부분만 빼올 수 있다.
#print(type(BeautifulSoup(response.text,'html.parser'))) #<class 'bs4.BeautifulSoup'>
# (데이터,파싱방법)
"""
데이터:
    - html
    - XML
파싱방법:
    - parsing
    - 의미있게 변경하는 방법
        - 문장, 문자열을 분석해서 의미가 있는 데이터로 변경
    - parser : html.parser (파이썬에서 기본적으로 지원해주는 parser)
"""
soup = BeautifulSoup(response.text,'html.parser')

# print(soup.title)
"""
<title>Daum</title>
"""
# print(soup.title.string)
"""
Daum
"""
# print(soup.span)
"""
html의 <span class span tag를 return
모든 span이 아니라 가장 상단에 위치한 tag
모든 span tag를 출력하고 싶다면
"""
# print(soup.findAll('span'))
"""
모든 span tag들이 list안에 저장되어 return
"""
#-----------------------------------------------------------------#
"""
html 파일로 저장하기
실시간 검색어
<a href=""
    - 모두 a tag
    - 모든 a tag가 실시간 검색어는 아니다.
    - class="link_favorsch @8"
"""
# file = open("daum.html","w")
# file.write(response.text)
# file.close()
#-----------------------------------------------------------------#
import requests
from bs4 import BeautifulSoup 

url = "http://www.daum.net/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

"""
html 문서에서 모든 a 태그를 가져오는 code
a 태그에는 span 등 실시간 검색어 이외에 여러가지가 들어있다.
"""
print(soup.findAll('a'))
"""
<a class="link_favorsch @6
실시간 검색어의 공통된 class를 활용

a 태그 중에 link_favorsch class만 찾아오기
"""
# print(soup.findAll('a','link_favorsch'))

#-----------------------------------------------------------------#
"""
보기 좋게 출력하기 위해서
다른 html요소를 제거

list로 return되어있다.
반복문을 활용하여 데이터를 하나씩 출력

result.get_text()
원하는 실시간검색어만 뽑아오기
"""
# results = soup.findAll('a','link_favorsch')

# i=0
# for result in results:
#     print(i+1,"위 : ",result.get_text(),'\n')
#     i+=1
#-----------------------------------------------------------------#
"""
몇월 며칠의 데이터인지
from datetime import datetime
datetime.today()
오늘 날짜 출력
2022-05-06 20:56:00.844390
보기 어렵고, 시간까지는 필요가 없다.

datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.")
"""

from datetime import datetime

# print(datetime.today())
print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

results = soup.findAll('a','link_favorsch')

i=0
for result in results:
    print(i+1,"위 : ",result.get_text(),'\n')
    i+=1
#-----------------------------------------------------------------#
"""
파일로 출력하기

파이썬으로 파일 다루기
open() - 내장함수
open(파일, 모드)
    - 파일 : 파일이름.확장자
    - 모드 : w : write : 쓰기 - 내용을 써 넣을 수 있다. 덮어쓰기
            r : read : 읽기 전용 - 내용을 쓰거나 더할수없다.
            a : append : 파일에 새로운 내용 추가 - 기존 내용을 보존
"""
search_rank_file = open('rankresult.txt','w')

# print(datetime.today())
print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

results = soup.findAll('a','link_favorsch')

i=0
for result in results:
    search_rank_file.write(str(i+1)+"위: "+result.get_text()+'\n')
    print(i+1,"위 : ",result.get_text(),'\n')
    i+=1

