from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import *
from . forms import *

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

@login_required(login_url='login')
def base(request):
    template_name = 'admin_royal_templates/base_admin.html'
    return render(request, template_name)

@login_required(login_url='login')
def home(request):
    template_name = 'admin_royal_templates/home_admin.html'
    return render(request, template_name)

@login_required(login_url='login')
def menu_investimentos(request):
    template_name = 'admin_royal_templates/investimentos.html'
    form = form_investimentos(request.POST or None)

    user = request.user

    if request.method == 'POST':
        if form.is_valid():
            investimento = form.save(commit=False)
            investimento.user = user
            investimento.save()
            messages.success(request, 'Investimento registrado com sucesso!')
            return redirect('admin_royal:home')
    else:
        form = form_investimentos()

    context = {
        'form': form
    }

    return render(request, template_name, context)

class response_invest(APIView):
    def get(self, _request):

        objs = Investimentos.objects.all()

        invest_serializer = InvestSerializer(objs, many=True)

        return Response({'data': invest_serializer.data})
