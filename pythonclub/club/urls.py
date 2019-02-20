from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('resource/', views.resource, name='resource'),
    path('meeting/', views.meeting, name='meeting'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='meetingdetail'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
    path('newresource/', views.newResource, name='newresource'),
]