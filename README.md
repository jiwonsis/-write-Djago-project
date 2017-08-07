# 파이썬 Django 학습
> 해당 소스는 무단 도용 배포 해도됩니다.
> 쉘 스크립트가 실행이 안될 경우 chmod 0700 [파일] 로 권한을 변경하시길 바랍니다.

### chapter.2 Blog Application 생성 및 DB연동
##### 1) Django 앱 생성 명령어로 blog 어플리케이션을 생성한다.
> 콘솔 :  python ./manage.py startapp blog
#### 2) blog 어플리케이션 DB Model 스키마 작성
> 참조 : https://docs.djangoproject.com/en/1.11/topics/db/models/
#### 3) 데이터 마이그래이션을 위한 settings.py -> INSTALLED_APPS에 'blog' 추가
#### 4) 데이터 마이그래이션 준비 및 DB 테이블에 추가
> 콘솔 :  python ./manage.py makemigrations blog
> 콘솔 :  python ./manage.py migrate
> 
> **개별적인 업데이트 및 이전 버전에 migration을 사용하고 싶다면?**
> 콘솔 : python ./manage.py sqlmigrate [앱이름] [마이그레이션 번호]
> 예) 콘솔 :  python ./manage.py sqlmigrate blog 0001
#### 5) 관리자 페이지에 blog 어플리케이션 데이터 모델 연동
> 일단 관리자 페이지에 접근할 수 있는 수퍼유저 생성
> 콘솔 : python ./manage.py createsuperuser
> 검증 = localhost:8000/admin으로 접속하여 로그인창에 수퍼유저로 접속 가능 유무 체크
#### 6) 관리자 페이지의 posts 어플리케이션 데이터 조회화면 튜닝
> blog/admin.py 파일에 post클래스 모델을 등록하고, 해당 화면을 튜닝한다.
#### 7) 블로그 모델 orm 쿼리 작성
> blog/models.py에 요청하고자 하는 함수 작성
> 참조 : https://docs.djangoproject.com/en/1.11/topics/db/queries/
> 참조 : http://raccoonyy.github.io/using-django-querysets-effectively-translate/