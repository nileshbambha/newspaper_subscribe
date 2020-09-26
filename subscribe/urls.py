from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('register.html',views.register,name='register'),
    path('login.html',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]
