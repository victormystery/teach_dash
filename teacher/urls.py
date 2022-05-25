from . import views

from django.urls import path

urlpatterns = [
    path('dashboard', views.teacher, name='dashboard'),
    path('', views.teachreg, name='registration'),
    path('login', views.teacherlogin, name='login'),
]