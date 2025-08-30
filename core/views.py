from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import *

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
