from django.urls import path
from .views import (
    home,
    room,
    createroom,
    updateroom,
    deleteroom,
    loginpage,
    logoutuser,
    registeruser,
    deletemessage,
    userprofile,
    updateuser,
    topicspage,
    activitypage,
)

app_name = 'base'

urlpatterns = [
    path('login/', loginpage, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('register', registeruser, name='register'),

    path('', home, name='home'),
    path('room/<int:id>/', room, name='room'),
    path('profile/<int:id>/', userprofile, name='userprofile'),

    path('create-room/', createroom, name='create-room'),
    path('update-room/<int:id>', updateroom, name='update-room'),
    path('delete-room/<int:id>', deleteroom, name='delete-room'),
    path('delete-message/<int:id>', deletemessage, name='delete-message'),

    path('update-user/', updateuser, name='update-user'),

    path('topics/', topicspage, name='topics'),
    path('activity/', activitypage, name='activity'),
]
