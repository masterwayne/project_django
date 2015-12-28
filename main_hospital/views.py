from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf 
from main_hospital.forms import RegistrationForm
from main_hospital.forms import AuthenticationForm

#def login(request):
#	c = {}
#	c.update(csrf(request))
#	return render_to_response('login.html',c)

def auth_view(request):
	if request.method== 'POST':
		username=request.POST.get('username','')
		password=request.POST.get('password','')
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=auth.authenticate(username=username,password=password)
			if user is not None:
				auth.login(request,user)
				return HttpResponseRedirect('/loggedin/')
		else:
			return HttpResponseRedirect('/invalid/')
        else:
		args = {}
		args.update(csrf(request))
		args['form']=AuthenticationForm()
		return render_to_response('login.html',args)

def loggedin(request):
	return render_to_response('loggedin.html',{'full_name':request.user.username})

def invalid_login(request):
	return render_to_response('invalid.html')

def logout(request):
	auth.logout(request)
	html="logout it is"
	return render_to_response('home.html')
def register_user(request):
	if request.method== 'POST':
		form= RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/register_success/')
	args = {}
	args.update(csrf(request))

	args['form']=RegistrationForm()
	
        return render_to_response('register.html',args)
def register_success(request):
	return render_to_response('home.html')
