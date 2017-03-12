from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^groups$', views.GroupsView.as_view(), name='groups'),
    url(r'^creategroup$', views.CreateGroupView.as_view(), name='create group')
    ]
