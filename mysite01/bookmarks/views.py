from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context, RequestContext
from django.template.loader import get_template
from bookmarks.models import User
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
				username = form.clean_data['username'],
				password = form.clean_data['password'],
				email = form.clean_data['email']

				)
			return HttpResponseRedirect('/')
	else:
		form = RegistrationForm()
	variables = RequestContext(request, {
		'form' : form
		})
	return render_to_response(
		'registration/register.html',
		variables
		
		)