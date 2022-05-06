import requests
import json
from datetime import datetime

city = 'Seoul'
apikey = '6f5b0c78c06671837ff7ba4d369fe932'
lang='kr'
units='metric'

api=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units={units}'

response = requests.get(api)
data = json.loads(response.text)

print(datetime.today().strftime("%Y년 %m월 %d일 %H시 %M분"))
#print(data)
"""
{
    'coord': {'lon': 126.9778, 'lat': 37.5683}, 
    'weather': [{'id': 804, 'main': 'Clouds', 'description': '온흐림', 'icon': '04n'}], 
    'base': 'stations', 
    'main': 
    {
        'temp': 16.66, 
        'feels_like': 16.55, 
        'temp_min': 14.69, 
        'temp_max': 16.66, 
        'pressure': 1017, 
        'humidity': 83, 
        'sea_level': 1017, 
        'grnd_level': 1010
    }, 
    'visibility': 10000, 
    'wind': 
    {
        'speed': 2.37, 
        'deg': 259, 
        'gust': 4.95
    }, 
    'clouds': {'all': 96},
     'dt': 1651849590, 
     'sys': {'type': 1, 'id': 5509, 'country': 'KR', 'sunrise': 1651869046, 'sunset': 1651919192}, 'timezone': 32400, 'id': 1835848, 'name': 'Seoul', 'cod': 200}
"""
print('날씨 : '+str(data['weather'][0]['description']))
print('온도 :'+str(data['main']['temp']))
print('체감온도 : '+str(data['main']['feels_like']))
print('최저 기온 : '+str(data['main']['temp_min']))
print('최고 기온 : '+str(data['main']['temp_max']))
sub_temp = data['main']['temp_max'] - data['main']['temp_min']
print('기온 차 : '+str(sub_temp))
print('습도 : '+str(data['main']['humidity']))