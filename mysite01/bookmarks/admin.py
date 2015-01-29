from django.contrib import admin

# Register your models here.
from bookmarks.models import *

class BookmarkAdmin(admin.ModelAdmin):
	fields = ['title','user','link']
#	fieldsets = [('Question Name', {'fields': ['question_text']}),('Date information', {'fields':['pub_date'], 'classes': ['collapse']}),]
#	inlines = [ChoiceInline]
	list_display = ('title', 'user', 'link')
	list_filter = ['user']
	search_fields = ['title']
	ordering = ('title',)

class SharedBookmarkAdmin(admin.ModelAdmin):
#	fields = ['bookmark','date','votes']
#	fieldsets = [('Question Name', {'fields': ['question_text']}),('Date information', {'fields':['pub_date'], 'classes': ['collapse']}),]
#	inlines = [ChoiceInline]
	list_display = ('bookmark','date','votes')
#	list_filter = ['user']
#	search_fields = ['title']

admin.site.register(Link)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag)
admin.site.register(SharedBookmark,SharedBookmarkAdmin)