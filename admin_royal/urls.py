from django.urls import path
from admin_royal import views
from admin_royal .views import *

app_name = "admin_royal"

urlpatterns = [
  path('', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),

  path('home/', views.home, name='home'),
  path('investimentos/', views.menu_investimentos, name='menu_invest'),

  # API class view comes above here
  path('response_invest/',  response_invest.as_view(), name='res_invest'),
]
