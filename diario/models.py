from django.conf import settings
from django.db import models


class Diario(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data = models.DateField()
    humor = models.IntegerField()
    texto = models.TextField()

    class Meta:
        unique_together = ('user', 'data')

    def __str__(self):
        return f"{self.user.username} - {self.data}"