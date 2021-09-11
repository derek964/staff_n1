from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def login(request):
    error_msg = ""
    if request.method == 'POST' and request.POST:
        username = request.POST['username']
        password = request.POST['password']
        userinfo = auth.authenticate(username=username, password=password)
        if userinfo:
            auth.login(request, userinfo)
            return redirect('/index/')
        else:
            error_msg = '用户名或密码错误'
    return render(request, 'login.html', {'error_msg': error_msg})

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def changepassword(request):
    if request.method == 'POST' and request.POST:
        oldpassword = request.POST['oldpassword']
        newpassword2 = request.POST['newpassword2']
        username = request.user
        userinfo = auth.authenticate(username=username, password=oldpassword)
        if userinfo:
            user = User.objects.get(username=username)
            user.set_password(newpassword2)
            user.save()
            result = True
            userinfo = auth.authenticate(username=username, password=newpassword2)
            auth.login(request, userinfo)
            return JsonResponse({'result': result})
        else:
            result = False
            return JsonResponse({'result': result})
    return render(request, 'changepassword.html', context=locals())

@login_required
def stat_staffinfo(request):
    return render(request, 'stat_staffinfo.html')

@login_required
def stat_projwork(request):
    return render(request, 'stat_projwork.html', context=locals())

@login_required
def staff_hire(request):
    return render(request, 'staff_hire.html', context=locals())

@login_required
def staff_hcmodify(request):
    return render(request, 'staff_hcmodify.html', context=locals())

@login_required
def staff_percent(request):
    return render(request, 'staff_percent.html', context=locals())

def logout(request):
    return render(request, 'logout.html')

