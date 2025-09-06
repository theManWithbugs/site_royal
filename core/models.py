from django.db import models

class Tamanho(models.Model):
    nome = models.CharField(max_length=50)  # Ex.: Pequena, Média, Grande
    diametro_cm = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)  # opcional

    def __str__(self):
        return self.nome

class Sabor(models.Model):
    nome = models.CharField(max_length=100)  # Ex.: Calabresa, Quatro Queijos
    descricao = models.TextField(blank=True, null=True)
    preco_adicional = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # ex: sabor especial custa mais

    def __str__(self):
        return self.nome

class Pizza(models.Model):
    tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE)
    sabores = models.ManyToManyField(Sabor, through="PizzaSabor")  # relação intermediária para casos meio-a-meio
    observacoes = models.TextField(blank=True, null=True)

    def calcular_preco(self):
        preco = self.tamanho.preco_base
        for sabor in self.sabores.all():
            preco += sabor.preco_adicional
        return preco

    def __str__(self):
        return f"Pizza {self.tamanho} - {', '.join([s.nome for s in self.sabores.all()])}"

class PizzaSabor(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    sabor = models.ForeignKey(Sabor, on_delete=models.CASCADE)
    proporcao = models.DecimalField(max_digits=4, decimal_places=2, default=1.0)  # 1.0 = sabor inteiro, 0.5 = meio a meio

    def __str__(self):
        return f"{self.sabor} ({self.proporcao * 100:.0f}%)"
