from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def stat_staffinfo(request):
    return render(request, 'stat_staffinfo.html')

def stat_projwork(request):
    return render(request, 'stat_projwork.html', context=locals())

def staff_hire(request):
    return render(request, 'staff_hire.html', context=locals())

def staff_hcmodify(request):
    return render(request, 'staff_hcmodify.html', context=locals())

def staff_percent(request):
    return render(request, 'staff_percent.html', context=locals())


