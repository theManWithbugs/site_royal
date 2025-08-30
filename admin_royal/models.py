from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Investimentos(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
  valor = models.IntegerField(blank=False, null=False)
  descricao = models.CharField(max_length=400, blank=True, null=True)
  data = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f"{self.user} {self.valor}"
