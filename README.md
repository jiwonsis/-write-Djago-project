# 파이썬 Django 학습
> 해당 소스는 무단 도용 배포 해도됩니다.
>
> 쉘 스크립트가 실행이 안될 경우 chmod 0700 [파일] 로 권한을 변경하시길 바랍니다.

### chapter.4 Blog 화면 연동 2 (기능추가)
##### 1) 페이지네이션 추가 및 ListView 연동
> blog/views.py 에 pagenation 추가후,  page객체로 템플릿에 전달
>
> 향후, 페이지 네이션 페이지가 추가될 경우, 대비하여 독립적인 템플릿으로 연동하여 사용처에서 가져오는 방식을 택함
> 
> 현재 학습 프로젝트에서는 '다음', '이전'으로 두개의 링크로 연동하였지만,  넘버링 방식으로도 연동 가능
> 
> 참조 : https://docs.djangoproject.com/en/1.11/topics/pagination/ [Django 페이지네이션 문서]
##### 2) 리펙토링을 해보자
> 함수처리에서 클래스 기반으로 listView를 작성해보자.
>
> blog/models -> post_list 함수의 경우는 해당 제너릭으로 간결하게 표현 가능.
>
> 간결하게 쓰인 PostListView의 경우를 URL 패턴 또한 간결하게 처리 가능.
