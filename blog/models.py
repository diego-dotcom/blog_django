from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    texto = models.TextField()
    fecha_creado = models.DateTimeField(default=timezone.now)
    fecha_publicado = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicado = timezone.now
        self.save()

    def __str__(self):
        return self.titulo

