"""
    랜덤으로 오늘 먹을 음식을 골라주기
    음식의 후보를 추가할 수도 있고, 뺄 수도 있게끔
    된장찌개, 피자, 제육볶음, 짜장면

    합집합(&)
    차집합(-)
    교집합(|)

    set으로 바꾸려면 먼저 list로 변환해야한다. -> set([])
"""
import time
import random

lunch = ['된장찌개','피자','제육볶음','짜장면']
# lunch.append('돈까스') #음식의 후보를 추가
# 사용자가 직접 추가할 수 있도록


while True:
    print(lunch)

    new_food = input('음식을 추가 해주세요: ')

    if (new_food == 'q') or (new_food =='Q'):
        break
    else:
        lunch.append(new_food)

print(lunch)

set_lunch = set(lunch)
while True:
    print(set_lunch)
    del_food = input('삭제할 음식 : ')

    if del_food == 'q':
        break
    else:
        set_lunch = set_lunch - set([del_food])

print(set_lunch, '중에서 선택합니다.')

for i in range(5,0,-1):
    print(i)
    time.sleep(1) #실제로 1초를 쉬는


final_food = random.choice(list(set_lunch))
print('선택된 음식은 ',final_food, '입니다.')
