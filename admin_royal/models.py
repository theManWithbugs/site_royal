from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Investimentos(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
  titulo = models.CharField(max_length=100, blank=False, null=False)
  valor = models.IntegerField(blank=False, null=False)
  descricao = models.CharField(max_length=400, blank=True, null=True, verbose_name='Descrição')
  data = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f"{self.user} {self.valor}"

  def save(self, *args, **kwargs):
    for field in self._meta.fields:
        value = getattr(self, field.name)
        if isinstance(field, models.CharField) and value is not None:
            setattr(self, field.name, value.upper())
        super().save(*args, **kwargs)