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
