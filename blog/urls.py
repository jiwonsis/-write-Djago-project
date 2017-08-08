from django.conf.urls import url
from . import views

urlpatterns = [
    # post 리스트 뷰 (root)
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    # post 디테일 뷰 (/년(4)/월(2)/일(2)/포스트 슬러그명)
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail, name='post_detail'),
]