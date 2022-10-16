from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = [
	path('', views.home, name='home'),
	path('menu/', views.menu, name='menu'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
]

urlpatterns += staticfiles_urlpatterns()