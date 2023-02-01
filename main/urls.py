from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = [
	path('', views.home, name='home'),
	path('menu/', views.menu, name='menu'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('edit_home/', views.edit_home, name='edit_home'),
	path('edit_about/', views.edit_about, name='edit_about'),
	path('edit_menu/', views.edit_menu, name='edit_menu'),
]

urlpatterns += staticfiles_urlpatterns()