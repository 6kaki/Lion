"""
둘은 같은 것을 의미
보편적으로는 MVC pattern이라고 하지만
Django 내에서는 MTV pattern이라고 한다.

MVC / MTV pattern
    - Web Framework는 비슷한 설계원칙을 따른다.
    - 방법, 순서, 단위가 다 비슷비슷
    - 데이터 베이스, html 관리, 내부동작 -- 3개의 단위
        1. DB와 상호작용
        2. 사용자들 눈에 보이는 부분
        3. 내부 동작의 논리를 담당하는 부분
    --> "디자인 패턴"

    - M : model : DB와 상호작용
    - V : view : 사용자 인터페이스 담당
    - C : controller : 웹 서비스 내부의 논리 담당

    - M : model : DB와 상호작용
    - T : Template : 사용자 인터페이스 담당
    - V : View : 웹 서비스 내부 동작의 논리를 담당

    - instagram
        - 사용자 : instagram.com (get 요청)
        - controller : html
        - View : html을 보여줌

        - 사용자 : 글작성 후 요청 (post 요청)
        - controller : 여기에 저장해야겠다.
        - Model : 글 저장
"""