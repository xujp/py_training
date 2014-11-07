from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from app01.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 's5web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
        (r'^$',index),
        (r'^linux/$',linux_bbs),
        (r'^python/$',python_bbs),
        (r'^login/$',login),
        (r'^login_auth/$',login_auth),
        (r'^logout/$',logout),
        (r'^detail/(\d+)/$',bbs_detail),
        (r'^create_article/$',create_article),
        (r'^submit_article/$',submit_article),
        (r'^sub_comment/$',sub_comment),
        (r'^sayHi/$',hello),
        (r'^sayhi/$',hi),
        (r'^second/$',second),
        (r'^time/plus/(\d+)/$',hours_plus),
)
