from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from django.contrib import auth,comments
from app01.models import *
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    print "========",request.user
    return render_to_response('index.html',{'user':request.user})

def linux_bbs(request):
	bbs_list = bbs.objects.filter(category = 'linux')
	return render_to_response("bbs_list.html",{'user':request.user,"bbs_list":bbs_list})

def python_bbs(request):
	bbs_list = bbs.objects.filter(category = 'python')
	return render_to_response("bbs_list.html",{'user':request.user,'bbs_list':bbs_list})

def login(request):
    return render_to_response("login.html")

def login_auth(request):
    print request.POST
    username,password = request.POST['username'],request.POST['password']
    user = auth.authenticate(username = username,password=password)
    print '+++++'
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect("/")
    else :
        return render_to_response("login.html",{'login_err':"Wrong user and password"})
		
def logout(request):
	c_user = request.user
	auth.logout(request)
	return HttpResponse("user %s logged out,please<a href='/login/'>click to re_login</a>"% c_user)
	
def bbs_detail(request,bbs_id):
	bbs_obj = bbs.objects.get(id=bbs_id)
	print bbs_obj
	return render_to_response("bbs_detail.html",{"bbs_obj":bbs_obj})

def create_article(request):
    return render_to_response("create_article.html")

def submit_article(request):
	bbs_title = request.POST.get('bbs_title')
	bbs_content = request.POST.get('bbs_content')
	bbs_category = request.POST.get('bbs_category')
	bbs.objects.create(
		title = bbs_title,
		content = bbs_content,
		category = bbs_category,
		author = User.objects.get(id = request.user.id),
		publish_date = datetime.datetime.now(),
		modify_date  = datetime.datetime.now(),
	)
	return HttpResponseRedirect("/%s/"%bbs_category)
	
def sub_comment(request):
	content_type = 7
	bbs_id = request.GET.get("bbs_id")
	print bbs_id
	comment = request.GET.get("text")
	sub_date = datetime.datetime.now()
	site = 1
	c = comments.Comment.objects.create(
		content_type_id = content_type,
		object_pk = bbs_id,
		site_id = site,
		user_id =request.user.id,
		comment = comment,
		submit_date = sub_date
	)
	c.save()
	return HttpResponseRedirect("/detail/%s/"%bbs_id)
	
def hello(request):
    ctime = datetime.datetime.now()
    name_list = ['alex','shawn','jack']
    for i in range(20):name_list.append(i)
    return render_to_response('hello.html',{'key':ctime,'name_info':name_list})

def hi(request):
    return HttpResponse("<h1 style='color:red'>hi world!</h1>")

def second(request):
    return HttpResponse(datetime.datetime.now())

def hours_plus(request,h):
    c_time = datetime.datetime.now()
    dt  = c_time + datetime.timedelta(hours=int(h))
    return HttpResponse('Current time is %s new time is %s'%(c_time,dt))
