
from django.conf.urls import include, url, patterns
from django.contrib.auth import views

from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('student_crud.urls')),
]
