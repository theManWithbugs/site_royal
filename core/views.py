from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from .ultils import get_carrinho
from django.http import HttpResponse

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
    return redirect('logout_page')

def pagina_logout(request):
    template_name= 'pagina_logout.html'
    return render(request, template_name)

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

#----------------------------------------------------------------------------#

#----------------------------------------------------------------------------#

#Função para limpar carrinho
# request.session.flush()

#View para ver carrinho aqui
def ver_carrinho(request):
    carrinho = get_carrinho(request)
    itens = carrinho.itens.all()  # todos os itens do carrinho
    total = sum(item.subtotal() for item in itens)  # soma dos subtotais

    carrinho_itens = CarrinhoItem.objects.values('carrinho__uuid', 'pizza__tamanho__nome', 'endereco__neighborhood').filter(carrinho=carrinho).first()

    context = {
        "carrinho": carrinho,
        "itens": itens,
        "total": total,
        "check_carrinho": carrinho_itens
    }
    return render(request, "carrinho.html", context)

def add_pizza_sel(request, id):
    tamanho = get_object_or_404(Tamanho, id=id)

    if request.method == 'POST':
        obs = request.POST.get('obs')
        pizza = Pizza.objects.create(tamanho=tamanho, observacoes=obs)

        total_sabores = 0
        for sabor in Sabor.objects.all():
            qtd = int(request.POST.get(f"sabor_{sabor.id}", 0))
            if qtd > 0:
                PizzaSabor.objects.create(pizza=pizza, sabor=sabor, quantidade=qtd)
                total_sabores += qtd

        if total_sabores > tamanho.max_sabores:
            pizza.delete()  # desfaz
            messages.error(request, f"O tamanho {tamanho.nome} permite no máximo {tamanho.max_sabores} sabores.")
            return redirect('add_pizza_sel', id=id)

        carrinho = get_carrinho(request)
        CarrinhoItem.objects.create(carrinho=carrinho, pizza=pizza)
        messages.success(request, "Pizza adicionada ao carrinho!")
        return redirect('carrinho')

    return render(request, 'add_pizza_sel.html', {
        'sabores': Sabor.objects.all(),
        'tamanho': tamanho,
        'id': id,
    })


def informar_endereco(request):
    template_name = 'inform_endereco.html'
    form = EnderecoForm(request.POST or None)

    carrinho = get_carrinho(request)

    if request.method == 'POST':
        if form.is_valid():
            # Salva o endereço primeiro para gerar o ID no banco
            endereco = form.save()

            # Pega todos os itens do carrinho
            carrinho_itens = CarrinhoItem.objects.filter(carrinho=carrinho)

            # Associa o endereço a cada item e salva
            for item in carrinho_itens:
                item.endereco = endereco
                item.save()

            messages.success(request, 'Endereço adicionado com sucesso!')
            return redirect('carrinho')
    else:
        form = EnderecoForm()

    return render(request, template_name, {'form': form})


#Only Action
def excluir_item(request, id):

    pizza_obj = get_object_or_404(Pizza, id=id)

    try:
        pizza_obj.delete()
        messages.success(request, 'Item excluido com sucesso!')
    except Exception as e:
        messages.error(request, f'Não foi possível realizar a ação: {e}')

    return redirect('carrinho')

def confirmar_pedido(request):
    carrinho = get_carrinho(request)  # Função que retorna o carrinho atual
    itens = carrinho.itens.all()

    if not itens.exists():
        return HttpResponse("Carrinho vazio!", status=400)

    # Pega o endereço do primeiro item (assumindo que todos têm o mesmo endereço)
    endereco = itens.first().endereco
    if not endereco:
        return HttpResponse("Endereço não definido!", status=400)

    # Cria o pedido
    pedido = PedidoRecebido.objects.create(carrinho=carrinho, endereco=endereco)

    # Debug: imprime todos os itens do carrinho
    for item in itens:
        print(f"{item.quantidade}x {item.pizza} - Endereço: {item.endereco}")

    return redirect('ped_finalizado')

def pedido_finalizado(request):
    template_name = 'nota_pedido.html'

    carrinho = get_carrinho(request)
    itens = carrinho.itens.all()

    context = {
        'itens': itens
    }

    return render(request, template_name, context)
