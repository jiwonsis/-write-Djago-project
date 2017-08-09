# 파이썬 Django 학습
> 해당 소스는 무단 도용 배포 해도됩니다.
> 쉘 스크립트가 실행이 안될 경우 chmod 0700 [파일] 로 권한을 변경하시길 바랍니다.

### Master Django 초기 세팅
해당 학습 프로젝트의 요건은 다음과 같습니다.

#### Dajngo DB
> Django에 기본으로 설정된 SQLite3를 사용하지 않습니다.
>
> MySQL5.7 버전을 사용합니다.
>
> Docker 어플리케이션을 사용하여 MySQL를 사용할 예정입니다.
> 
> MySQL DB 환경 설정은 다음과 같습니다.
> > 테이블 케릭터셋 : utf8-mb4
> >
> > 컬렉션 서버 : utf8mb4_unicode_ci
> >
> > 사유:  MySQL의 경우는 아시아 언어 지원 및 Emoji(A.K.A 이모티콘)를 사용하기 위해서 입니다.

#### Docker
> 현재 진행중입니다.
> 
> 현재까지는 MySql만 도커로 사용하는 방식을 채택하였습니다.
>
> docker를 기본적으로 설치했다는 가정하에 도커 파일을 실행시키시면 됩니다.
> 
> 도커 이미지 생성
>> 콘솔 : cd docker/mysql
>> 콘솔 : docker build -t mysqldev:1 .
>
> 도커 서버 생성 및 실행
> > 콘솔 :  cd docker/mysql
> > 콘솔 :  chmod 0700 ./create_mysql_docker.sh
> > 콘솔 :  ./create_mysql_docker.sh
> 
> 도커 서버 중지
> > 콘솔 : docker stop mysqldev:1
>
> 도커 서버 실행
> > 콘솔 : docker start mysqldev:1
>
> 도커 설치 및 자세한 사항은 아래의 참조를 참고 하세요
>
> 참조 : https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html [도커 설치]
> 참조 : http://pyrasis.com/private/2014/11/30/publish-docker-for-the-really-impatient-book [도커의 전반적인 내용을 다룬 도커 서적입니다]

#### Django 프로젝트 세팅 
> Django-1.11버전(현재 최신 릴리즈 버전) 지원 RDBMS
>> - SQLite3(기본설정)
>> - PostgreSQL
>> - MySQL (해당 프로젝트 설정)
>> - Oracle
>> 
>
> Django 캐쉬 
>> *현재는 기본설정인 메모리 캐쉬로 하고 있습니다.*
>> 
>> 향후 : Redis 또는 파이어베이스로 할 예정입니다.
>>
>> 참조 : https://docs.djangoproject.com/en/1.11/ref/settings/#backend [캐시 설정 부분]
>>
>> 참조 : https://github.com/sebleier/django-redis-cache [래디스 캐시 패키지]
>
> 다국어 지원
>> 현재는 다국어를 안하고 있지만, 향후 진행할 예정입니다.
>>
>> 참조 : https://docs.djangoproject.com/en/1.11/ref/settings/#languages [다국어 설정] 

#### IDE 세팅
> 현재 제가 하고 있는 IDE는 Pycharm Professional로 작업하여 VirtualENV 설정은 IDE가 자동으로 담당하게 설정되어 있습니다.
>
> 항후, Pycharm Community 버전으로도 브랜치 생성하여 공유하도록 하겠습니다.