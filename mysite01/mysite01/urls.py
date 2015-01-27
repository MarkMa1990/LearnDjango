from django.conf.urls import include, url
from django.contrib import admin
from bookmarks.views import *
from django.views.generic import TemplateView

import os.path
site_media = os.path.join(
	os.path.dirname(__file__), 'site_media'
	)

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Browsing
    url(r'^$', main_page),
    url(r'^admin/', include(admin.site.urls)),

    # Session management
    url(r'^user/(\w+)/$', user_page),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media}),
    url(r'^register/$', register_page),
    url(r'^register/success/$', TemplateView.as_view(template_name='registration/register_success.html')),

    # Account management
    url(r'^save/$', bookmark_save_page),


]
