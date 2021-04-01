from django.contrib import admin
from django.urls import path, include
from myapp import views

app_name='myapp'

urlpatterns = [
    path('user/', views.register, name='register'),
    path('login/', views.userlogin, name='userlogin'),
    path('logout/', views.userlogout, name='userlogout'),
    path('login/exam/', views.exam, name='exam'),
    path('login/exam/<int:exam_id>', views.question, name='question'),
    path('login/marks/<int:exam_id>', views.marks, name='marks'),


]
