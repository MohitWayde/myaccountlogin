from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from accounts import views

urlpatterns = [
    path('', views.index,name='index'),
    path('signin', views.signin,name='signin'),
    path('signup', views.signup,name='signup'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('logout',views.logout_user,name='logout'),
]
