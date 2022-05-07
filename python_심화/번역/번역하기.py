"""
번역기

from googletrans import Translator

언어 감지 / 번역 라이브러리
    - 언어감지 : 안녕하세요 : 한국어
             : hello : 영어
            - 언어를 감지해주는 기능
    - 번역
        - 안녕하세요 -> hello
        - 뜻을 파악하고 다른 언어로 변경해준다.


"""     

from googletrans import Translator

#print(Translator)
#<class 'googletrans.client.Translator'>

"""
언어 감지하기

    1. 번역기를 만든다.
        - Translator()
    2. 언어감지를 원하는 문장을 설정한다.
        
    3. 언어를 감지한다.
        - 언어감지 결과물 = 번역기.detect(text)
        - 언어감지결과물.lang : 'ko' 한국어로 감지
"""
# # 1.
# translator = Translator()

# # 2.
# #sentence = "안녕하세요 코드라이언입니다."
# sentence = input("언어감지할 문장을 입력하세요 : ")

# # 3.
# detected = translator.detect(sentence)
# #Detected(lang=ko, confidence=None)
# #confidence
# #언어감지 결과물

# print(detected.lang)
#ko

"""
번역하기

    1. 번역기를 만든다.
        - Translator()
    2. 번역을 원하는 문장을 설정한다.
        - input()
    3. 번역을 원하는 언어를 설정한다.
        - dest = 'en'
    4. 번역한다.
        - .translate(text,dest,src)
        - dest : 어떤 언어로 변역을 할 것인지 (destination)
            - 언어표기는 https://py-googletrans.readthedocs.io/en/latest/ 여기서 확인
        - src : source text의 언어 (optional) 알아서 언어를 감지할 수 있다.
"""     

#1.
translator = Translator()

#2.
sentence = input("번역하고 싶은 문장을 입력하세요 : ")
country_dict = {
    '프랑스':'fr',
    '베트남':'vi',
    '스페인':'es',
    '중국':'zh-CN',
    '아랍':'ar',
    '독일':'de',
    '몽골':'mn',
    '힌디':'hi'
}

choice_lang = input("언어 선택: ")
country = country_dict[choice_lang]

#sentence = input('번역을 원하는 문장을 입력하세요 : ')

#3.
result=translator.translate(sentence, country)
#Translated(src=ko, dest=en, text=Hello, this is Code Ryan., pronunciation=None, extra_data="{'confiden...")
detected = translator.detect(sentence)

print("="*36)
print(detected.lang,' : ',sentence)
print(result.dest," : ",result.text)
print("="*36)


