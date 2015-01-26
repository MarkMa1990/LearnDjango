from django.conf.urls import include, url
from django.contrib import admin
from bookmarks.views import main_page, user_page, logout_page, register_page

import os.path
site_media = os.path.join(
	os.path.dirname(__file__), 'site_media'
	)

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', main_page),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/(\w+)/$', user_page),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media}),
    url(r'^register/$', register_page),

]
