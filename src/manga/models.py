from django.db import models
from django.contrib.auth.models import User

class Manga(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario que lo guardó
    title = models.CharField(max_length=200)
    manga_id = models.CharField(max_length=50)  # ID de la API (ej: MangaDex)
    description = models.TextField(blank=True)
    cover_url = models.URLField()
    status = models.CharField(max_length=20, choices=[
        ('reading', 'Leyendo'),
        ('completed', 'Completado'),
        ('planned', 'Planeado')
    ])
    rating = models.IntegerField(null=True, blank=True)  # 1-5 estrellas

    def __str__(self):
        return self.title