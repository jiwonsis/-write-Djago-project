# 파이썬 Django 학습
> 해당 소스는 무단 도용 배포 해도됩니다.
>
> 쉘 스크립트가 실행이 안될 경우 chmod 0700 [파일] 로 권한을 변경하시길 바랍니다.

### chapter.3 Blog 어플리케이션 화면 개발
##### 1) 화면을 구성할 요소를 정의한다. (a.k.a 컨트롤러 구성)
> Blog 화면의 구성은 2가지로 한다.
>
> post는 model 클래스의 orm호출하여 가져온다.
>
> listView :  post들 중에서 published가 된 상태값의 post들을 모와서 리스트로 구성
>
> detailView :  특정한 post (여기서도 published로 상태값의 된 post)의 내용으로 구성
>
> detailView에서 정의한 년/월/일/포스트 URL의 경우의 조회값이 URL로 호출되기 때문에, 추가적으로 
##### 2) 화면을 구성한 컨트롤러의 함수를 URL로 연동하자
> URL로 연동하기 앞서 Django의 URL 표현은 python3 URL 정규식을 사용한다.
> 
> 이는 브라우저 주소필드에 입력하는 값을 개발자의 의도대로 제어하기 위함이다.
>
> 참조 : https://docs.python.org/3/howto/regex.html [파이썬3 정규식]
>
> 참조 : https://docs.djangoproject.com/en/1.11/topics/http/urls/ [Django URL 디스패치]
> 
> blog/urls.py에 URL 패턴과 view의 함수와 고유식별자 이름을 추가한다.
>
> root/urls.py에 블로그 어플리케이션 URL또한 추가한다.
>
> **콘솔 : python ./manage.py runserver로 구동하면, 템플릿이 없다고 뜨는데 이는 정상이다!**
##### 3) 템플릿 만들기
> 해당 템플릿 엔진의 경우는 jinja와 Django template중에서 해당 학습에서는 Django template로 선정하여 템플릿 작업을 하였다.
>
> 템플릿에서 주요 기능인 filter, block 등의 기능의 대한 자세한 레퍼런스를 참조하길 바한다.
>
> 참조 : https://docs.djangoproject.com/en/1.11/topics/templates/ [템플릿 엔진 설정과 지원 템플릿 엔진]
>
> 참조 :  https://docs.djangoproject.com/en/1.11/ref/templates/language/ [Django 템플릿 엔진]
>
> 참조 :  https://docs.djangoproject.com/en/1.11/ref/templates/builtins/ [Django 템플릿 빌드]
##### 번외) 이슈처리
> 템플릿 엔진을 사용할때 다양한 이슈가 발생되기도 한다. 그중 한예로 학습에 포함시켰다.
>
> 해당 이슈는 템플릿에서 조합하여 처리할 수도 있지만, 객체에서 그대로 넘겨주는 방법으로 구현하였다.
> 
> **이슈발생!**
>
> listView 각 리스트마다 a 링크의 href링크를 걸어줘야 한다. 하지만 해당 href로 전달하는 요소는 컨트롤러에는 있지만 템플릿으로 넘기는 요소에는 나와있지 않다.**
> 
> **어떻게 보안할 것인가? (이슈 해결 계획)**
>
> "해당 이슈는 post 오브젝트에 링크URL를 담는 방법으로 템플릿에서 간편하게 사용하는 방법으로 진행할 계획이다."
>  
> **해결! (계획 이행)**
> blog>models.py 에 함수를 지정하여, 쿼리셋을 조합하여 post 클래스 객체에 추가
