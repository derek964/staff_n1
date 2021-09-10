from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def login(request):
    if request.method == 'POST' and request.POST:
        username = request.POST['username']
        password = request.POST['password']
        userinfo = auth.authenticate(username=username, password=password)
        if userinfo:
            auth.login(request, userinfo)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

@login_required
def index(request):
    return render(request, 'index.html')

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

