from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restwithmproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
# aruna
    url(r'^admin/', include(admin.site.urls)),
)
