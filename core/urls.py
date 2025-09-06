from django.urls import path
from core import views
from core.views import *

urlpatterns = [
    path('base/', views.base_view, name="base"),
    path('', views.login_cliente, name="login_cliente"),
    path('logout/', views.logoutView, name='logout'),
    path('home', views.home_view, name="home"),
    path('home/add_items/', views.add_items, name='add_items'),


    path('form_cadastro/', views.formulario_cadastro, name='form_cadastro'),
]
