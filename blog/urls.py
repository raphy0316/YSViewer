from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), #게시물 리스트
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), #게시물 상세보기
    url(r'^post/new/$', views.post_new, name='post_new'), #게시물 생성
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'), #게시물 수정
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'), #게시물 임시저장
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'), #게시물 게시
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'), #게시물 삭제

    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'), #댓글 달기
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'), #댓글 삭제

    url(r'^upload/$', views.model_form_upload, name='model_form_upload'), #파일 업로드
    url(r'^files/$', views.file_list, name='file_list'), #파일 리스트
    url(r'^files/(?P<pk>\d+)/$', views.file_detail, name='file_detail'), #파일 상세보기
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
