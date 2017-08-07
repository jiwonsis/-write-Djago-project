# 파이썬 Django 학습
> 해당 소스는 무단 도용 배포 해도됩니다.
> 쉘 스크립트가 실행이 안될 경우 chmod 0700 [파일] 로 권한을 변경하시길 바랍니다.

### chapter.1 Django 초기 세팅
> 1) 파이썬 3.6.x 버전의 파이썬을 설치한다. (Mac OS 경우는 2.7버전이기 때문에 버전업을 시켜야함.)
> 2) Virtual ENV 설정한다. (Pycharm 으로 하면 편리함.)
> 3) 기본 SQLLite 를 사용하지 않고 MySql 를 사용한다. (Docker를 설치하여 진행하시기 바랍니다.)
> 
>> docker 설치 및 mysql 로컬 서버 실행
>> 콘솔: docker pull mysql
>
>> 콘솔: ./create_mysql_docker.sh
>
>> 만일,  제시작을 하실 경우 콘솔: ./restart_mysql_server.sh
>
>> 해당 pip 인스톨하기 콘솔: ./pip_install.sh
