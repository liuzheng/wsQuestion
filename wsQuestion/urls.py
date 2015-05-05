from django.conf.urls import include, url, patterns
from django.contrib import admin
import os

urlpatterns = [
    # Examples:
    # url(r'^$', 'wsQuestion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += patterns('wsQuestion.views',
        (r'^$','index'),
        )
