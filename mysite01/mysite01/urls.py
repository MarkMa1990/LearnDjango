from django.conf.urls import include, url
from django.contrib import admin
from bookmarks.views import main_page, user_page
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', main_page),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/(\w+)/$', user_page)
]
