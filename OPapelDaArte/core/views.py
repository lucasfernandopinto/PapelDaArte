from django.shortcuts import render
from core.models import Artista, Obras, Noticia
import random


# Create your views here.

def index(request):
    # aux = random.randrange(1, 1, 1)
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'index.html', dados)


def artista(request, art_sobrenome):
    # aux = random.randrange(1, 1, 1)
    dados = {'artista': Artista.objects.all(),
             'artistaPrincipal': Artista.objects.filter(art_sobrenome=art_sobrenome),
             'obras': Obras.objects.filter(obr_artista__in=Artista.objects.filter(art_sobrenome=art_sobrenome)),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'artista.html', dados)


def julioReis(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'julioReis.html', dados)


def oPapelDaArte(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'oPapelDaArte.html', dados)


def hitoriaGravura(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'hitoriaGravura.html', dados)


def tecnicasImpressao(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'tecnicasImpressao.html', dados)


def emolduramento(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'emolduramento.html', dados)


def noticias(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'noticias.html', dados)


def artigos(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'artigos.html', dados)


def entrevistas(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'entrevistas.html', dados)


