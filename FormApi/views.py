
from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponse
from FormApi.models import Users,Context_for_year
import FormApi.Constant 
from django.views.decorators.csrf import csrf_exempt
from FormApi.form import SendEmailForm,UsersForm
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@csrf_exempt
def Login(request):
	if request.method == "POST":
		username = request.POST[Constant.Username]
		password = request.POST[Constant.Password]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("/Sendmail")
		message = "Login falied,error login"
		return render(request,"login.html",{'message':message})
	elif request.user.is_authenticated:
		return redirect(Sendmail)
	else:
		return render(request,"login.html")
		
	
def Logout(request):
	logout(request)
	return redirect(Login)




@csrf_exempt
def FillData(request):
	data = json.loads(request.body)	
	try:
		username = str(data[Constant.Username])
	except:
		return HttpResponse("username not provided")

	try:
		email = str(data[Constant.Email])
	except:
		return HttpResponse("email not provided")
	
	try:
		phone = str(data[Constant.Phone])
	except:
		phone = str(Constant.empty)

	try:
		year = int(data[Constant.Year])
	except:
		year = 2015
	try:
		rollno = str(data[Constant.Rollno])
			
	except:
		rollno = ""	
	newuser = Users.objects.create(UserName = username,Email=email,Phone=phone,Rollno=rollno,Year=year)
	newuser.save()

	json_form = json.dumps({Constant.Username:newuser.UserName,
				Constant.Year:newuser.Year,
				Constant.Rollno:newuser.Rollno,
				Constant.Email:newuser.Email,
				Constant.Phone:newuser.Phone})
	print(json_form)

	return HttpResponse(json_form,content_type=Constant.content_type)


@login_required
def Sendmail(request):
	log = 0
	if request.method == 'POST':
		SendEmailform = SendEmailForm(request.POST)
		if SendEmailform.is_valid():
			subject = SendEmailform.cleaned_data[Constant.Subject]
			body = SendEmailform.cleaned_data[Constant.Body]
			value1 = SendEmailform.cleaned_data[Constant.Sorting]
			for year in value1:
				values = Users.objects.filter(Year=int(year))
				Email(values,subject,body)

			return HttpResponse("Email send succesfully")
		return HttpResponse("error during validation of form")
	else:
		SendEmailform = SendEmailForm()
		return render(request,'form.html',{'SendEmailform':SendEmailform})
def ViewDatabase():
	return HttpResponse("Database")


def Email(userlist,subject,body):
	for user in userlist:
		email1 = user.Email
		email = EmailMessage(subject,body,to=[email1])
		value = email.send()
