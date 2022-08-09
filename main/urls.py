from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('products/', views.products, name='products'),
	path('products/regular/', views.regular, name='regular'),
	path('products/seasonal/', views.seasonal, name='seasonal'),
	path('about', views.about, name='about'),
	path('contact', views.contact, name='contact'),
]