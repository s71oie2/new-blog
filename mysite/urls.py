from django.conf.urls import url, include # include('bookmark.urls') 함수
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('bookmark.urls')),
]


