import requests
from bs4 import BeautifulSoup
from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://www.nate.com/'

response=requests.get(url,headers=headers)

soup = BeautifulSoup(response.content,'html.parser')

#print(soup)

results = soup.findAll('span','txt_rank')

search_file = open('nate_search.txt','w')

print(datetime.today().strftime("%Y년 %m월 %d일 실시간 검색어 순위\n"))

rank=1
for result in results:
    search_file.write(str(rank)+"위 : "+result.get_text()+'\n')
    print(str(rank)+"위 : "+result.get_text()+'\n')
    rank+=1

"""
code가 잘못되지 않았더라도
특정 웹사이트의 경우 불법으로 페이지의 정보를 크롤링하지 못하게하려고 차단
로봇이 아닌경우 다른 방법을 사용해야함
    - 아래와 같은 구문을 추가해야함
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
response = requests(url,headers=headers)

로봇이 아님을 알려주는 구문

그래도 안되는데
"""