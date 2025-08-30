from django.urls import path
from admin_royal import views

urlpatterns = [
  path('', views.login_view, name='login'),
  path('home/', views.home, name='home'),
  path('investimentos/', views.menu_investimentos, name='menu_invest'),
]