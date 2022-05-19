from django.urls import path,include
from .views import *
from.import views


urlpatterns = [
    path('', views.loginUser, name ="login"),
    path('logout/', views.logoutUser, name ="logout"),
    path('register/', views.registerUser, name ="register"),
    path('index/', index, name= 'index'),
    path('ajax/', ajax, name= 'ajax'),
    path('scan/',scan,name='scan'),
    path('profiles/', profiles, name= 'profiles'),
    path('details/', details, name= 'details'),

    path('add_profile/',add_profile,name='add_profile'),
    path('edit_profile/<int:id>/',edit_profile,name='edit_profile'),
    path('delete_profile/<int:id>/',delete_profile,name='delete_profile'),


    path('clear_history/',clear_history,name='clear_history'),
    path('reset/',reset,name='reset'),


]
