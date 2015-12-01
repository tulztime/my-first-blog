# We also want to keep the mysite/urls.py file clean, so we will 
# import urls from our blog application to the main mysite/urls.py file.

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]
