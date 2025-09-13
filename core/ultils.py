from .models import *

def get_carrinho(request):
    """
    Retorna o carrinho do usuário (pelo uuid salvo na sessão).
    Se não existir, cria um novo.
    """
    cart_id = request.session.get("cart_id")

    if cart_id:
        try:
            carrinho = Carrinho.objects.get(uuid=cart_id)
        except Carrinho.DoesNotExist:
            carrinho = Carrinho.objects.create()
            request.session["cart_id"] = str(carrinho.uuid)
    else:
        carrinho = Carrinho.objects.create()
        request.session["cart_id"] = str(carrinho.uuid)

    return carrinho