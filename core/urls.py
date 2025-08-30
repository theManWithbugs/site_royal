from django.urls import path
from core import views
from core.views import *

urlpatterns = [
    path('base/', views.base_view, name="base"),
    path('', views.home_view, name="home"),
    path('home/add_items/', views.add_items, name='add_items'),
]