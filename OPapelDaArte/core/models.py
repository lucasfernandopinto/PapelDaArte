from django.db import models


# Create your models here.

class Artista(models.Model):
    art_nome = models.CharField(max_length=100)
    art_sobrenome = models.CharField(max_length=100)
    art_imagem = models.CharField(max_length=80)
    art_desc = models.TextField(blank=True, null=True)
    art_nascimento = models.IntegerField(null=True)
    art_morte = models.IntegerField(null=True)

    class Meta:
        db_table = 'artista'

    def __str__(self):
        return self.art_sobrenome


class Obras(models.Model):
    obr_img = models.CharField(max_length=100)
    obr_legenda = models.CharField(max_length=200, null=True)
    obr_nome = models.CharField(max_length=200)
    obr_ano = models.IntegerField(null=True)
    obr_valor = models.FloatField(null=True)
    obr_status = models.CharField(max_length=50, null=True)
    obr_info = models.TextField(null=True)
    obr_artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

    class Meta:
        db_table = 'obras'

    def __str__(self):
        return self.obr_nome


class Noticia(models.Model):
    not_nome = models.CharField(max_length=100)
    not_tipo = models.CharField(max_length=15)
    not_desc = models.TextField()
    not_imagem = models.CharField(max_length=80)

    class Meta:
        db_table = 'noticias'

    def __str__(self):
        return self.not_nome
