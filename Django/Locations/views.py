import datetime
from .models import locations
from . import serializers
from rest_framework import viewsets
from django.template import Context
from django.utils import timezone
from django.contrib import messages
from .serializers import locationsapiserializer
from django.template.loader import get_template
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as out
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect

# Show your views here.
def home(request):
	username = None
	#if request.user.is_authenticated():
	context,uname = {},{}
	request.session.set_test_cookie()
	context['dataset'] = locations.objects.all()
	context['uname'] = request.user.username
	return render(request,'home.html',context)

def index(request):
	request.session.set_test_cookie()
	context = {}
	context['uname'] = request.user.username
	return render(request,'index.html',context)

def addmod(request):
	context = {}
	context['uname'] = request.user.username
	return render(request,'add.html',context)

# Create your views here.
def add(request):
	context = {}
	if request.method == 'POST':
		context['uname'] = request.user.username
		print(context)
		request.session.set_test_cookie()
		get_LOC = request.POST.get('location')
		get_CITY = request.POST.get('city')
		get_COUNTRY = request.POST.get('country')
		val = locations(location=get_LOC,city=get_CITY,country=get_COUNTRY)
		messages.success(request, "Done")
		finVal = val.save()
	return render(request,'add.html',context)

# Delete your views here.
def delete(request,id):
	print(id)
	if request.method == 'POST':
		request.session.set_test_cookie()
		pi = locations.objects.get(pk=id)
		pi.delete()

	return HttpResponseRedirect('/home')

# Update your views here.
def update(request,id):
	if request.method == 'POST':
		context = {}
		context['uname'] = request.user.username
		request.session.set_test_cookie()
		context['pi'] = locations.objects.get(pk=id)
	return render(request,'del.html',context)

# Login
def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			auth_login(request,user)
			fname =  user.username
			print(fname)
			return render(request,"index.html",{'uname':fname})
		else:
			messages.error(request,"Bad Cred")
			return render(request,'login.html')

	return render(request,'login.html')
# Logout
def logout(request):
	request.session.set_test_cookie()
	out(request)
	return render(request,'login.html')

# Update 2
def updated(request):
	if request.method == 'POST':
		context = {}
		context['uname'] = request.user.username
		request.session.set_test_cookie()
		get_ID = request.POST.get('id')
		get_LOC = request.POST.get('location')
		get_CITY = request.POST.get('city')
		get_COUNTRY = request.POST.get('country')
		get_DATE = request.POST.get('date')
		val = locations(id=get_ID,location=get_LOC,city=get_CITY,country=get_COUNTRY,date=timezone.now())
		finVal = val.save()
	return HttpResponseRedirect('/home')

# API
class LocationsViewSet(viewsets.ModelViewSet):
	queryset = locations.objects.all()
	serializer_class = serializers.locationsapiserializer
