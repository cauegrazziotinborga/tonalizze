from django.db import models
from django.contrib.auth.models import User

class TonalidadeConfig(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tonalidade_config')
    tonalidade_1 = models.IntegerField(default=50)
    tonalidade_2 = models.IntegerField(default=50)
    tonalidade_3 = models.IntegerField(default=50)

    def __str__(self):
        return f'Config de {self.user.username}'