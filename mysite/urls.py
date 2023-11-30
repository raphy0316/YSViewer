from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), #관리자 페이지
    url(r'^accounts/login/$', login, name='login'), #로그인
    url(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page': '/'}), #로그아웃
    url(r'', include('blog.urls')), #blog/urls.py
    url(r'^accounts/signup/$', views.CreateUserView.as_view(), name = 'signup'), #회원가입
    url(r'^accounts/signup/done/$', views.RegisteredView.as_view(), name = 'create_user_done'), #회원가입 완료
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
