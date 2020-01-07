from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
from .models import User, Photo, Followers
from .forms import *
from django.contrib.auth import authenticate, login, logout as dlogout
import json

def ajaxsignup(request):
	ajax = AjaxSignUp(request.POST)
	context = {'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)

def ajaxsavephoto(request):
	ajax = AjaxSavePhoto(request.POST, request.user)
	context = { 'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)

def ajaxlikephoto(request):
	ajax = AjaxLikePhoto(request.GET, request.user)
	context = { 'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)

def ajaxtag(request):
	ajax = AjaxTagPhoto(request.GET, request.user)
	context = { 'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)

def ajaxfollow(request):
	ajax = AjaxFollow(request.GET, request.user)
	context = { 'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)

def ajaxsetprofilepic(request):
	ajax = AjaxSetProfilePic(request.POST, request.user)
	context = { 'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)

def ajaxphotofeed(request):
	ajax = AjaxPhotoFeed(request.GET, request.user)
	context = { 'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)

def ajaxprofilefeed(request):
	ajax = AjaxProfileFeed(request.GET, request.user)
	context = { 'ajax_output': ajax.output() }
	return render(request, 'ajax.html', context)

def ajaxlogin(request):
	ajax = AjaxLogin(request.POST)
	logged_in_user, output = ajax.validate()
	if logged_in_user != None:
		login(request, logged_in_user)
	context = {'ajax_output': output}
	return render(request, 'ajax.html', context)

def signup(request):
	context = {}
	return render(request, 'sign-up.html', context)

def home(request):
	context = {}
	if request.user.is_authenticated:
		u = User.objects.filter(username=request.user.username)[0]
		if u.profilepic == "":
			u.profilepic = "static/assets/img/default.png"

		url_parameter = request.GET.get("q")
		if url_parameter:
			users = User.objects.filter(username__icontains=url_parameter)
		else:
			users = ''

		context["users"] = users
		if request.is_ajax():

			html = render_to_string(
				template_name="users-search-result.html", context={"users": users}
			)
			data_dict = {"html_from_view": html}
			return JsonResponse(data=data_dict, safe=False)

		context = { 'user': request.user, 'ProfilePic': u.profilepic}
		return render(request, 'logged-in-index.html', context)

	return render(request, 'index.html', context)

def profile(request, username):
	if User.objects.filter(username=username).exists():
		u = User.objects.filter(username=username)[0]
		if not Followers.objects.filter(user=username, follower=request.user.username).exists():
			following = "Follow"
		else:
			following = "Unfollow"

		if u.profilepic == "":
			u.profilepic = "static/assets/img/default.png"
		context = { "ProfilePic": u.profilepic, "whosprofile": username, "logged_in_as": request.user.username, "following": following }
		if request.user.is_authenticated:
			return render(request, 'logged-in-profile.html', context)
		return render(request, 'profile.html', context)
	else:
		return redirect(home)

def search(request):
	if request.method == 'GET':
		search = request.GET['search']

		return redirect("/"+search)

	# users = User.objects.all()
	# return JsonResponse({'users':users})

def upload(request):
	form = UploadForm()
	print(form.media)
	return render(request, 'upload.html', { 'form': form })

def logout(request):
	context = {}
	dlogout(request)
	return redirect(home)
