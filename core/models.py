from django.db import models
import uuid

class Carrinho(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return str(self.uuid)

class CarrinhoItem(models.Model):
    carrinho = models.ForeignKey("Carrinho", on_delete=models.CASCADE, related_name="itens")
    pizza = models.ForeignKey("Pizza", on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.pizza.calcular_preco() * self.quantidade

    def __str__(self):
        return f"{self.quantidade}x {self.pizza}"

class Tamanho(models.Model):
    nome = models.CharField(max_length=50)  # Ex.: Pequena, Média, Grande, GG
    diametro_cm = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    max_sabores = models.PositiveIntegerField(default=1)  # limite de sabores
    preco_base = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nome

class Sabor(models.Model):
    nome = models.CharField(max_length=100)
    preco_adicional = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nome

class Pizza(models.Model):
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    sabores = models.ManyToManyField(Sabor)
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')

    def calcular_preco(self):
        """Soma o preço base do tamanho com os adicionais de cada sabor"""
        return self.tamanho.preco_base + sum(s.preco_adicional for s in self.sabores.all())

    def __str__(self):
        # ⚠️ Não acessa M2M aqui para evitar RecursionError
        return f"Pizza {self.tamanho.nome}"
