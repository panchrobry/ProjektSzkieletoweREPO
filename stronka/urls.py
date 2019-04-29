from django.conf.urls import url
from . import views
from django.urls import path, include
from django.contrib.auth.views import login,logout


urlpatterns = [
    url(r'^login/$',login, {'template_name': 'accounts/login.html' }),
    url(r'^home/$',views.home),
    path('accounts/', include('django.contrib.auth.urls')),
    #url(r'^logout/$',logout, {'template_name': 'accounts/logout.html' }),
    url(r'^register/$',views.register, name = 'register'),
    url(r'^contact/$',views.contact, name = 'contact'),
    url(r'^addrobot/$',views.addRobot, name = 'addRobot'),
    url(r'^addteam/$',views.addTeam, name = 'addTeam'),

    url(r'^registerOwn/$',views.registerUserOwn, name = 'registerUserOwn'),
]
