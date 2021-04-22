from random import randint

from django.db import models


# Create your models here.
from django.db.models import Count


class Artista(models.Model):
    art_nome = models.CharField(max_length=100)
    art_sobrenome = models.CharField(max_length=100)
    art_imagem = models.ImageField(upload_to='Artistas')
    art_desc = models.TextField(blank=True, null=True)
    art_nascimento = models.IntegerField(null=True)
    art_morte = models.IntegerField(null=True)

    class Meta:
        db_table = 'artista'

    def __str__(self):
        return self.art_sobrenome


class ObrasManager(models.Manager):
    def random(self):
        count = self.aggregate(ids=Count('id'))['ids']
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class Obras(models.Model):
    obr_img = models.ImageField(upload_to='Obras')
    obr_legenda = models.CharField(max_length=200, null=True)
    obr_nome = models.CharField(max_length=200)
    obr_ano = models.IntegerField(null=True)
    obr_valor = models.FloatField(null=True)
    obr_status = models.CharField(max_length=50, null=True)
    obr_info = models.TextField(null=True)
    obr_artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

    objects = ObrasManager()

    class Meta:
        db_table = 'obras'

    def __str__(self):
        return self.obr_nome


class NoticiaManager(models.Manager):
    def random(self):
        count = self.aggregate(ids=Count('id'))['ids']
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class Noticia(models.Model):
    not_nome = models.CharField(max_length=100)
    not_tipo = models.CharField(max_length=15)
    not_desc = models.TextField()
    not_imagem = models.ImageField(upload_to='Artigos')

    objects = NoticiaManager()

    class Meta:
        db_table = 'noticias'

    def __str__(self):
        return self.not_nome
