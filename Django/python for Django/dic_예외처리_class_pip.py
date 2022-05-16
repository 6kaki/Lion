"""
웹 프레임워크
    - 웹서비스를 "쉽게" 만들어주는 기계
    - 쉽게 : 사용법이 "정형화"되어있는 기계
    - 쓰이는 문법만 자주 사용된다. (basic level에서는)
"""

"""
dictionary 자료형
    - 사전형 자료형
    - 무작위적인 데이터를 하나의 이름으로 묶으려면 -> 대응
    - 대응이 되는 데이터를 표현해주는 자료형
    - (김연아, 박찬호, 마이클조던, 손흥민, 피겨스케이팅, 야구, 농구, 축구) - 운동선수
    - 왜 사전형이라고 불리우는지?
        - 탐색의 기준 : z --> key
        - 찾고자하는 값 : zip --> value
        - 탐색의 기준을 통해 찾고자하는 값을 얻는다.
    - 딕셔너리를 언제 사용하는가?
        - N x 2 표를 통해 데이터를 표현하고 싶을 때

    - val = {key1:value1, key2:value2, ...}
        - key1 -> value1에 대응
    - key값은 "중복"되거나 "변하면" 안된다.
    - value값 얻기
        - val[key1] => value1
    - 새로운 데이터쌍 추가
        - val[새로운 key] = 새로운 value

"""

"""
예외처리
    - 프로그램을 "멈춤 없이" 실행시킬 수 있다.
        -https://docs.python.org/ko/3/tutorial/errors.html
    - 실사용자가 사용할때는 예외처리가 꼭 필요하다.
    - python의 오류
        - 문법에러(파싱 에러)와 예외

            - 파싱 에러 : 오타 혹은 문법적인 오류
                - SyntaxError:invalid syntax
                - 실행자체가 불가능한 오류
                - ex) : 이 입력되지 않아서 실행할 수 없다.
                    def main(a,b)
                        return a+b
                    
            - 예외
                - 프로그램 실행 자체를 멈추지는 않는 오류
                - 실행 중 감지되는 오류
                    - 0으로 나누기
                        - ZeroDivisionError
                    - 정의되지 않은 변수
                        - NameError
                    - 자료형이 맞지 않는 오류 등
                        - TypeError

    - 모든 오류를 알고 출시할 수는 없다.
    - 오류를 Handling하는 방법
    - try:
        일단 시도해볼 구문
        오류가 생길 수 있는 구문
    - except 발생오류:
        오류가 발생할 경우 실행할 코드

    - ex)
        try:
            4/0
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다.")

    - 그냥 except: 만 사용하면 어떤 오류라도 다 
        try:
            4/0
        except:
            print("0으로 나눌 수 없습니다.")
    
    - finaly:
        오류가 발생하든 안하든
        최종적으로 무조건 실행할 코드

"""

"""
클래스와 객체
    - 왜?
        - 모든 것을 프로그래밍하고 싶어서
        - 모든 다른 "대상"을 관찰 -> "객체"를 관찰
        - 세상에 있는 객체는 무엇으로 구성되어있는가?
            - "상태"와 "동작"으로 나타낼 수 있다.
            - "변수"와 "함수"로 나타낼 수 있다.
            - 비행기
            - 상태
                life = 2
                bullet = 100
            - 동작
                def attack():
                    if 스페이스바:
                        공격
        - 비행기는 한두개가 아니다.
            - 여러개로 만들 수 있어야한다.
            - "한번에 여러개 정의할 수 있는 방법"

        - 상태와 동작을 한번에 여러개 정의할 수 있는 방법 ==> 객체지향프로그래밍(OOP)
        - class로 틀을 설계하고 찍어낸다.
            class 이름: -> 비행기 설계
                변수들(상태)
                함수들(동작)
            
            객체이름1 = 클래스이름() -> 비행기1
            객체이름2 = 클래스이름() -> 비행기2
            객체이름3 = 클래스이름() -> 비행기3
        
"""

"""
모듈, 패키지, 라이브러리 (pip)
    - 모듈
        - 파이썬으로 정의된 파일, 함수, 변수 등 가장 작은 단위
        - a.py, b.py
        - a.py 안에 def sum 내용을 b.py에서 사용하고 싶다면?
            - import a
            - a.sum()

    - 패키지
        - 모듈의 집합
        - 3개의 파이썬 file(save.py, get.py, delete.py)
            -> data 폴더에 담겨져있다.
        - 1개의 파이썬 file(app.py) + data폴더 
            -> myproject 폴더에 담겨있다.
        - data => 패키지
        - in app.py
            import data.save
            import data.get
            import data.delete

    - 라이브러리
        - 쓸만한 기능들을 모듈/패키지로 만들어 놓은 것
        - 미리 준비된 모듈/패키지
        - python standard library : 파이썬에서 미리 만들어 놓은 라이브러리
        - pypi : 사람들이 직접 만들어서 올려놓은 것
            pypi.org

    - 다운로드한 패키지를 관리해주는 tool
        - pip
        - pip install package이름==version
        - pip search
        - pip uninstall 
        - pip freeze 다운받은 패키지 목록 조회
        
"""

