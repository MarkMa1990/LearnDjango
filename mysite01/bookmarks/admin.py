from django.contrib import admin

# Register your models here.
from bookmarks.models import *
admin.site.register(Link)
admin.site.register(Bookmark)
admin.site.register(Tag)
admin.site.register(SharedBookmark)