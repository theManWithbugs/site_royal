from django.db import models
import uuid
from django.utils import timezone

class Carrinho(models.Model):
    #Como estou usando default, sempre que é criado um carrinho novo o django cria um uuid
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return str(self.uuid)


class Tamanho(models.Model):
    nome = models.CharField(max_length=50)
    max_sabores = models.PositiveIntegerField(default=1)
    preco = models.DecimalField(max_digits=6, decimal_places=2)  # <-- preço da pizza deste tamanho

    def __str__(self):
        return self.nome

class ImgItems(models.Model):
    nome_item = models.CharField(max_length=80)
    arq = models.FileField(upload_to='img')

    def __str__(self):
        return self.nome_item

class Sabor(models.Model):
    nome = models.CharField(max_length=100)
    img_obj = models.ForeignKey(
        ImgItems,
        on_delete=models.CASCADE,
        related_name='objeto_img',
        blank=True,
        null=True,
        verbose_name='imagem'
    )
    preco_adicional = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nome

class Pizza(models.Model):
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    observacoes = models.TextField(blank=True, null=True)
    sabores = models.ManyToManyField(Sabor, through='PizzaSabor', blank=True)

    def __str__(self):
        return f"{self.tamanho.nome}"

    def calcular_preco(self):
        """
        Retorna o preço da pizza baseado no tamanho.
        Aqui você pode adicionar lógica extra, se quiser, por exemplo, cobrar por sabor adicional.
        """
        return self.tamanho.preco


class PizzaSabor(models.Model):
    """Relação intermediária que permite repetir sabores e definir quantidades"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    sabor = models.ForeignKey(Sabor, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.sabor.nome} ({self.quantidade}x)"

class ClienteAdress(models.Model):
    street = models.CharField(max_length=400, blank=None, null=False, verbose_name="Rua")
    neighborhood = models.CharField(max_length=200, blank=None, null=False, verbose_name="Bairro")
    number = models.IntegerField(blank=None, null=False, verbose_name="Número")
    client_phone = models.CharField(blank=None, null=False, verbose_name="Número para contato", max_length=11)
    reference = models.CharField(max_length=400, blank=True, null=True, verbose_name="Ponto de referência")

    def __str__(self):
        return f"Bairro: {self.neighborhood} | Rua: {self.street} | Número: {self.number}"

class CarrinhoItem(models.Model):
    carrinho = models.ForeignKey("Carrinho", on_delete=models.CASCADE, related_name="itens")
    pizza = models.ForeignKey("Pizza", on_delete=models.CASCADE)
    endereco = models.ForeignKey("ClienteAdress", on_delete=models.CASCADE, related_name="endereco", null=True, blank=True)
    quantidade = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.pizza.calcular_preco() * self.quantidade

    def __str__(self):
        return f"{self.quantidade}x {self.pizza}"

class PedidoRecebido(models.Model):
    carrinho = models.ForeignKey("Carrinho", on_delete=models.CASCADE)
    endereco = models.ForeignKey("ClienteAdress", on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.carrinho.uuid}"
