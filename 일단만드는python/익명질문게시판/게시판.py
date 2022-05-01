"""
이상형이 뭐에요

질문을하고 답을하는 프로그램
질문을 입력해주세요: 
q 더이상 질문을 받지 않고 대답으로 넘어감
앞에서 적은 질문이 차례대로 나오고 거기에 대답
>>> 답변을 입력해주세요:

질문과 대답을 정리해서 출력

어떻게 저장할지
두가지로 나눠서 저장
질문 : key
답변 : value
>>> dictionary{key:value}
>>> {질문:답변},{질문:답변},{질문:답변}
>>> [{질문:~},{답변:~}]
Django를 들으면 웹으로 구현할 수 있다.
"""
total_dictionary = {}

while True:
    Q = input('질문을 입력해주세요 : ')
    if Q == 'q':
        break
    else:
        total_dictionary[Q]=''
        
for i in total_dictionary.keys():
    print(i)
    A = input('답변을 입력해주세요 : ')
    total_dictionary[i] = A

print(total_dictionary)
