from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [

    path('', views.home, name = 'home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('contact/', views.contact, name='contact'),
    path('c/', views.c, name='c'),
    path('python/', views.python, name='python'),
    path('java/', views.java, name='java'),
    path('HTML/', views.HTML, name='HTML'),
    path('Css/', views.Css, name='Css'),

]
