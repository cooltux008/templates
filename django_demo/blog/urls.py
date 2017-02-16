from django.conf.urls import include, url   
from django.contrib import admin   
from app import views   
   
urlpatterns = [   
    # Examples:   
    # url(r'^$', 'myblog.views.home', name='home'),   
    # url(r'^blog/', include('blog.urls')),   
   
    url(r'^admin/', include(admin.site.urls)),   
    url(r'^hello/$', views.hello, name='hello world'),   
    url(r'^$', views.index, name='homepage'),   
]
