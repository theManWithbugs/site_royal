from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from . forms import *

# def login_cliente(request):
#     template_name = 'login_cliente.html'

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Login ou senha incorretos!')

#     return render(request, template_name)

def logoutView(request):
    auth_logout(request)
    return redirect('login_cliente')

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

def base_view(request):
    template_name = 'base.html'
    return render(request, template_name)

def home_view(request):
    template_name = 'home.html'
    return render(request, template_name)

def add_items(request):
    template_name = 'add_pizza.html'
    form_pizza = AddPizzaForm(request.POST or None)
    form_sabor = AddSaborForm(request.POST or None)

    if request.method == 'POST':
        if 'submit_pizza' in request.POST:
            if form_pizza.is_valid():
                form_pizza.save()

        elif 'submit_sabor' in request.POST:
            if form_sabor.is_valid():
                form_sabor.save()

    else:
        form_pizza = AddPizzaForm()
        form_sabor = AddSaborForm()

    context = {
        'form_pizza': form_pizza,
        'form_sabor': form_sabor,
    }

    return render(request, template_name, context)
