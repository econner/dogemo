from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import accounts.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dogemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', accounts.views.index, name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
