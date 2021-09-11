from django.conf.urls import url
from staff.views import *

urlpatterns = [
    url(r'^$', login),
    url(r'^index', index),
    url(r'^stat_staffinfo', stat_staffinfo),
    url(r'^stat_projwork', stat_projwork),
    url(r'^staff_hire', staff_hire),
    url(r'^staff_hcmodify', staff_hcmodify),
    url(r'^staff_percent', staff_percent),
    url(r'^logout', login),
    url(r'^changepassword', changepassword),
    ]
