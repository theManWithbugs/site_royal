from django.urls import path
from admin_royal import views
from admin_royal .views import *

app_name = "admin_royal"

urlpatterns = [
  path('', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),

  path('home/', views.home, name='home'),
  path('investimentos/', views.menu_investimentos, name='menu_invest'),
  path('home/reg_items/', views.reg_items_view, name='reg_items'),

  # API class view comes above here
  path('response_invest/',  response_invest.as_view(), name='res_invest'),
  path('response_titulo/', response_titulo.as_view(), name='res_titulo'),
]
