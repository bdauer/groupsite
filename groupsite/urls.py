from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^groups$', views.GroupsView.as_view(), name='groups'),
    url(r'^creategroup$', views.CreateGroupView.as_view(), name='create group'),
    url(r'^updategroup/(?P<pk>[0-9]+)/$', views.ManageGroupView.as_view(), name='update group'),
    url(r'^groupdetails/(?P<pk>[0-9]+)/$', views.GroupDetailView.as_view(), name='group detail')
    ]
