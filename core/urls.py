from django.urls import path
from core import views
from core.views import *

urlpatterns = [
    path('base/', views.base_view, name="base"),
    path('login/', views.login_cliente, name="login_cliente"),
    path('logout/', views.logoutView, name='logout'),
    path('pagina_logout/', views.pagina_logout, name='logout_page'),

    path('', views.home_view, name="home"),

    #Tratando aqui
    # path('home/add_items/', views.add_items, name='add_items'),

    path('carrinho/', views.get_or_create_cart, name="add_cart"),
    path('home/pizzas_available/', views.pizzas_available, name='pizzas_dispo'),
    path('home/drinks_available/', views.drinks_available, name='drinks_dispo'),

    path('form_cadastro/', views.formulario_cadastro, name='form_cadastro'),

    path('pagina_test/', views.pagina_teste, name='teste'),

    #Paginar de add item selecionado
    path('home/add_pizza_sel/<int:id>/', views.add_pizza_sel, name='add_pizza_sel'),

    #Items vinculados ao UUID especifico
    path('home/carrinho/', views.ver_carrinho, name='carrinho'),

    path('excluir_item/<int:id>/', views.excluir_item, name='excluir_item'),
    path('carrinho/infor_endere/', views.informar_endereco, name='info_adress'),

    path('confirmar_pedi/', views.confirmar_pedido, name='confirm_pedid'),
    path('pedido_finalizado/', views.pedido_finalizado, name='ped_finalizado')
]
