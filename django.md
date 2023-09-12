## Django
#### framework : 웹 애플리케이션을 빠르게 개발할 수 있도록 구조, 규칙, 라이브러리 등을 제공하는 패키지 도구 (ex- Express.js, Django, Spring 등)<br/>
-> 기본 요소를 제외한 핵심 기능에 선택과 집중 가능, 생산성 극대, 유지보수와 확장에 용이

#### Django: python 기반의 웹 프레임 워크 

- 클라이언트와 서버 <br/>
![](data:image/png;base64,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)

웹에서 어떠한 사이트를 방문할때 클라이언트(ex-chrome)는 방문할 사이트 서버에 서비스를 요청한다. 그러면 서버는 데이터베이스에서 해당 파일을 찾아 클라이언트의 요청에 응답한다. 부가적으로 크롬과 같은 웹 브라우저는 사용자가 전달받은 페이지를 볼 수 있도록 해석해서 제공해주게 된다. <br/>
-> django라는 프레임워크를 통해 서버를 구현할 수 있다..!!

#### 가상환경과 전역환경
- 전역환경: 로컬 컴퓨터에서 사용중인 모든 라이브러리
- 가상환경: python 및 python 패키지들로부터 독립적인 가상의 작업 환경

- 가상환경이 필요한 이유: 작업 툴의 버전이 상이하거나 패키지의 충돌 가능성 문제를 예방


#### django로 서버를 구현해보자
```
1. 가상환경 만들기
$ python -m venv venv
2. 가상환경 on(activate)
$ source nenv/Scripts/activate
3. django 설치
$ pip install django
4. 패키지 목록 얼리고 파일로 저장
$ pip freeze > requirements.txt
**패키지 목록에 있는 툴 설치하기**
pip install -r requirements.txt
5. 프로젝트 생성
$ django-admin startproject firstpjt . 
6. 어플리케이션(기능) 생성
python manage.py startapp articles
7. 어플리케이션 등록
project > settings > installed_apps의 맨 윗줄에 어플리케이션 이름 작성
```

#### 디자인패턴
- MVC/MTV : 애플리케이션을 구조화하는 대표적인 패턴으로 공통적인 문제를 해결하기 위한 해결책의 관행. (이런 패턴으로 만들면 에러를 방지하기 쉽다!)
- Model : 데이터베이스
- view/templates : 사이트에 보여질 시각적 요소
- controller/view : 시스템 동작들(요청/응답)

#### 프로젝트 구조
1. setting.py - 프로젝트의 모든 설정 관리
2. urls.py - URL과 적절한 views를 연결시켜줌
3. init__.py - 해당 폴더를 패키지로 인식하도록 설정
4. asgi.py - 비동기식 웹 서버와의 연결 관련 설정
5. wsgi.py - 웹 서버와의 연결 관련 설정
6. manage.py - 사용가능한 명령어들 모음

#### 앱 구조
1. admin.py - 관리자용 페이지 설정
2. models.py - 데이터베이스와 관련해 model을 정의
3. views.py - 서비스 요청에 대한 응답을 반환
4. apps.py - 앱에 대한 정보
5. tests.py - 프로젝트 테스트 코드를 작성하는 곳

#### 서버에서 직접 요청을 받아 응답해보자
```
1. URLs
URLs 파일에서 요청받은 서비스를 view로 연결해주는 코드를 작성
앱 패키지에서 view 모듈 가져오기 > 경로(서비스 주소, 적용할 함수) 작성해주기

2. view
views 파일에서 요청받은 서비스를 처리하는 함수를 작성
반드시 함수의 매개변수는 request인자로 받고, return render사용하기

3. template
해당되는 앱에 경로를 만들어주고 html형태의 template생성

4. 서버 실행
$ python manage.py runserver

**서버 종료**
$ ctrl+c
```



