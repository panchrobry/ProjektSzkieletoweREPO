from django.conf.urls import url
from . import views
from django.urls import path, include
from django.contrib.auth.views import login,logout


urlpatterns = [
    url(r'^login/$',views.login_view, name = 'login_view'),
    url(r'^home/$',views.home),
    url(r'^robots/$',views.view_robots, name = 'view_robots'),
    url(r'^createMatchLegoSumo/$',views.createMatchLegoSumo, name = 'createMatchLegoSumo'),
    url(r'^createMatchSumo/$',views.createMatchSumo, name = 'createMatchSumo'),
    url(r'^createMatchMiniSumo/$',views.createMatchMiniSumo, name = 'createMatchMiniSumo'),
    url(r'^addraceLegoLF/$',views.createRaceLegoLF, name = 'createRaceLegoLF'),
    url(r'^addraceLF/$',views.createRaceLF, name = 'createRaceLF'),
    url(r'^logout/$',views.logout_view, name = 'logout'),
    url(r'^register/$',views.register, name = 'register'),
    url(r'^contact/$',views.contact, name = 'contact'),
    url(r'^addrobot/$',views.addRobot, name = 'addRobot'),
    url(r'^addteam/$',views.addTeam, name = 'addTeam'),
    url(r'^jointeam/$',views.joinTeam, name = 'joinTeam'),
    url(r'^registerOwn/$',views.registerUserOwn, name = 'registerUserOwn'),
    url(r'^change/$',views.change, name = 'change'),
    url(r'^changePassword/$',views.changePassword, name = 'changePassword'),
    url(r'^matches/$',views.matches, name = 'matches'),
    url(r'^team/$',views.team, name = 'team'),
    url(r'^export/$',views.export, name = 'export'),
    url(r'^races/$',views.races, name = 'races'),
    url(r'^groupAuto/$',views.AutoGroup, name = 'AutoGroup'),
    url(r'^groupManualLegoSumo/$',views.ManualGroupLegoSumo, name = 'ManualGroupLegoSumo'),
    url(r'^groupManualMiniSumo/$',views.ManualGroupMiniSumo, name = 'ManualGroupMiniSumo'),
    url(r'^groupManualSumo/$',views.ManualGroupSumo, name = 'ManualGroupSumo'),
    url(r'^judgePanel/$',views.judgePanel,name='judgePanel'),
    url(r'^successPage/$',views.successPage,name='successPage'),
]
