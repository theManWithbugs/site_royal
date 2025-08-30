from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    template_name = 'admin_royal_templates/login.html'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Login ou senha incorretos!')

    return render(request, template_name)

def base(request):
    template_name = 'admin_royal_templates/base_admin.html'
    return render(request, template_name)

def home(request):
    template_name = 'admin_royal_templates/home_admin.html'
    return render(request, template_name)

@login_required
def menu_investimentos(request):
    template_name = 'admin_royal_templates/investimentos.html'
    return render(request, template_name)