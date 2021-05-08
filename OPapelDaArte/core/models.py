from random import randint

from django.db import models


# Create your models here.
from django.db.models import Count


class Artista(models.Model):
    art_nome = models.CharField("Nome do artista", max_length=100)
    art_sobrenome = models.CharField("Sobrenome do artista:", max_length=100)
    art_imagem = models.ImageField("Imagem do artista:", upload_to='Artistas')
    art_desc = models.TextField("Texto descritivo:", blank=True, null=True)
    art_nascimento = models.IntegerField("Ano de nascimento", null=True)
    art_morte = models.IntegerField("Ano de falecimento", null=True)
    art_legenda = models.CharField("Legenda do Artista", max_length=200, null=True)

    class Meta:
        db_table = 'artista'

    def __str__(self):
        return self.art_sobrenome


class ObrasManager(models.Manager):
    def random(self):
        count = self.aggregate(ids=Count('id'))['ids']
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class Obra(models.Model):
    OPTIONS = (
        ('D', 'Disponível'),
        ('V', 'Vendida')
    )
    obr_img = models.ImageField("Selecione a obra:", upload_to='Obras')
    obr_legenda = models.CharField("Legenda da obra", max_length=200, null=True)
    obr_nome = models.CharField("Nome da obra:", max_length=200)
    obr_ano = models.IntegerField("Ano de publicação:", null=True)
    obr_valor = models.FloatField("Valor da obra:", null=True)
    obr_status = models.CharField("Estado da obra:", max_length=50, null=True, choices=OPTIONS)
    obr_info = models.TextField("Adicione as informações adicionais da obra:", null=True)
    obr_artista = models.ForeignKey(Artista, on_delete=models.CASCADE, verbose_name='Artista:')

    objects = ObrasManager()

    class Meta:
        db_table = 'obra'

    def __str__(self):
        return self.obr_nome


class NoticiaManager(models.Manager):
    def random(self):
        count = self.aggregate(ids=Count('id'))['ids']
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class Noticia(models.Model):
    OPTIONS = (
        ('N', 'Notícia'),
        ('A', 'Artigo'),
        ('E', 'Entrevista'),
    )
    not_nome = models.CharField("Nome da publicação:", max_length=100)
    not_tipo = models.CharField("Tipo da publicação:", max_length=1, choices=OPTIONS)
    not_desc = models.TextField("Faça a descrição da sua publicação:")
    not_imagem = models.ImageField("Selecione a imagem da publicação:", upload_to='Artigos')
    not_publi = models.DateField("Data de publicação")
    not_legenda = models.CharField("Legenda da noticia", max_length=200, null=True)

    objects = NoticiaManager()

    class Meta:
        db_table = 'noticias'

    def __str__(self):
        return self.not_nome
