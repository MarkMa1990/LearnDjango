from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context, RequestContext
from django.template.loader import get_template
from bookmarks.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from bookmarks.forms import *

def main_page(request):
	return render_to_response(
		'main_page.html', RequestContext(request)
#		{ 'user': request.user}
		)
#	template = get_template('main_page.html')
#	variables = Context( {
#		'head_title': 'Django Bookmarks',
#		'page_title': 'Welcome to Django Bookmarks',
#		'page_body' : 'Where you can store and share bookmarks!'
#		'user': request.user
#		})
#	output = template.render(variables)
#	return HttpResponse(output)

def user_page(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('Requseted user not found!')

	bookmarks = user.bookmark_set.all()
	template = get_template('user_page.html')
	variables = RequestContext(request, {

		'username' : username,
		'bookmarks': bookmarks,

		})
	output = template.render(variables)
	return HttpResponse(output)

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

def register_page(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password2'],
				email = form.cleaned_data['email']

				)
			return HttpResponseRedirect('/register/success/')
	else:
		form = RegistrationForm()
	variables = RequestContext(request, {
		'form' : form
		})
	return render_to_response(
		'registration/register.html',
		variables
		
		)

def bookmark_save_page(request):
	if request.method == 'POST':
		form = BookmarkSaveForm(request.POST)
		if form.is_valid():
			# Create or get link.
			link, dummy = Link.objects.get_or_create(
				url= form.cleaned_data['url']
				)
			# Create or get bookmark.
			bookmark, created= Bookmark.objects.get_or_create(
				user=request.user,
				link=link
				)
			# Update bookmark title.
			bookmark.title = form.cleaned_data['title']
			# If the bookmark is being updated, clear old tag list.
			if not created:
				bookmark.tag_set.clear()
			# Create new tag list.
			tag_names = form.cleaned_data['tags'].split()
			for tag_name in tag_names:
				tag, dummy = Tag.objects.get_or_create(name=tag_name)
				bookmark.tag_set.add(tag)
			# Save bookmark to database.
			bookmark.save()
			return HttpResponseRedirect(
				'/user/%s/' % request.user.username
				)
	else:
		form = BookmarkSaveForm()
	variables = RequestContext(request, {
		'form': form
		})
	return render_to_response('bookmark_save.html', variables)


