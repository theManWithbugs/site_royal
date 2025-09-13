from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .ultils import get_carrinho

from . forms import *

#Account
#----------------------------------------------------------------------------#

#----------------------------------------------------------------------------#
def login_cliente(request):
    template_name = 'login_cliente.html'
    if request.method == 'POST':
        telefone = request.POST.get('telefone')
        senha = request.POST.get('senha')

        try:
            user = User.objects.get(telefone=telefone)
            user = authenticate(request, username=user.username, password=senha)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login_cliente')
        except User.DoesNotExist:
            messages.error(request, 'Usuario não registrado!')
            return redirect('login_cliente')

    return render(request, template_name)

def logoutView(request):
    auth_logout(request)
    return redirect('login_cliente')

#Add new user
def formulario_cadastro(request):
    template_name = 'login_cliente.html'

    if request.method == 'POST':
        telefone = request.POST.get('telefone')
        senha = request.POST.get('password')

        if User.objects.filter(telefone=telefone).exists():
            messages.error(request, "Telefone já cadastrado!")
            return render(request, template_name)

        user = User.objects.create_user(username=telefone, password=senha)

        user.telefone = telefone
        user.save()

        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect('login_cliente')

    return render(request, template_name)
#----------------------------------------------------------------------------#

#----------------------------------------------------------------------------#

#Main pages
#----------------------------------------------------------------------------#

#----------------------------------------------------------------------------#
def base_view(request):
    template_name = 'base.html'
    return render(request, template_name)

def home_view(request):
    template_name = 'home.html'
    return render(request, template_name)
#----------------------------------------------------------------------------#

#----------------------------------------------------------------------------#

#Products
#----------------------------------------------------------------------------#

#----------------------------------------------------------------------------#
def pagina_teste(request):
    template_name = 'pagina_test.html'

    pizzas = Pizza.objects.all()

    return render(request, template_name, {'pizzas': pizzas})

def get_or_create_cart(request):
    cart_id = request.COOKIES.get("cart_id")

    if cart_id and Carrinho.objects.filter(uuid=cart_id).exists():
        cart = Carrinho.objects.get(uuid=cart_id)  # só recupera
    else:
        cart = Carrinho.objects.create()  # cria um novo

    return cart

def pizzas_available(request):
    template_name = 'pizzas.html'
    return render(request, template_name)

def drinks_available(request):
    template_name= 'drinks.html'
    return render(request, template_name)

#Tratando aqui
# def add_items(request):
#     template_name = 'add_pizza.html'
#     form_pizza = AddPizzaForm(request.POST or None)

#     if request.method == 'POST':
#         if form_pizza.is_valid():
#             pizza = form_pizza.save(commit=False)
#             pizza.save()
#             form_pizza.save_m2m()

#             carrinho = get_carrinho(request)
#             CarrinhoItem.objects.create(carrinho=carrinho, pizza=pizza)

#             messages.success(request, "Pizza adicionada ao carrinho!")
#             print(carrinho)
#             return redirect('add_items')

#     return render(request, template_name, {'form_pizza': form_pizza})

#----------------------------------------------------------------------------#

#----------------------------------------------------------------------------#

#Função para limpar carrinho
# request.session.flush()

#View para v er carrinho aqui
def ver_carrinho(request):
    carrinho = get_carrinho(request)
    itens = carrinho.itens.all()  # todos os itens do carrinho
    total = sum(item.subtotal() for item in itens)  # soma dos subtotais

    context = {
        "carrinho": carrinho,
        "itens": itens,
        "total": total,
    }
    return render(request, "carrinho.html", context)

def add_pizza_sel(request, id):
    template_name = 'add_pizza_sel.html'

    #Quando se preciso de apenas um objeto é utilizado get_object_or_404
    tamanho = get_object_or_404(Tamanho, id=id)

    form_pizza = AddPizzaForm(request.POST or None, tamanho=tamanho)
    if request.method == 'POST':
        if form_pizza.is_valid():
            pizza = form_pizza.save(commit=False)
            pizza.tamanho = tamanho
            try:
                pizza.save()
                form_pizza.save_m2m()
            except Exception as e:
                messages.error(f"Ocorreu um erro: {e}")

            carrinho = get_carrinho(request)
            CarrinhoItem.objects.create(carrinho=carrinho, pizza=pizza)

            messages.success(request, "Pizza adicionada ao carrinho!")
            print(carrinho)
            return redirect('add_pizza_sel', id)

    return render(request, template_name, {'form_pizza': form_pizza, 'id': id})

def excluir_item(request, id):

    pizza_obj = get_object_or_404(Pizza, id=id)

    try:
        pizza_obj.delete()
        messages.success(request, 'Item excluido com sucesso!')
    except Exception as e:
        messages.error(request, f'Não foi possível realizar a ação: {e}')

    return redirect('carrinho')