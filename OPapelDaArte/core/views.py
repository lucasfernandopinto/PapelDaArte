from django.contrib.auth.decorators import login_required
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


def historiaGravura(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'historiaGravura.html', dados)


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


def historiaSeculo19(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'seculo19.html', dados)


def historiaBrasil(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'brasil.html', dados)


def aguaForte(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'aguaForte.html', dados)


def aguaTinta(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'aguaTinta.html', dados)


def buril(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'buril.html', dados)


def heliogravura(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'heliogravura.html', dados)


def linoleo(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'linoleo.html', dados)


def litografia(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'litografica.html', dados)


def maneiraNegra(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'maneiraNegra.html', dados)


def pontaSeca(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'pontaSeca.html', dados)


def processoAcucar(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'processoAcucar.html', dados)


def processoEnxofre(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'processoEnxofre.html', dados)


def processoLavis(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'processoLavis.html', dados)


def processoRelevo(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'processoRelevo.html', dados)


def serigrafia(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'serigrafia.html', dados)


def vernizMole(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'vernizMole.html', dados)


def xilogravura(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'xilogravura.html', dados)


@login_required(login_url='login/')
def adicionarArtista(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'addArtista.html', dados)


@login_required(login_url='login/')
def adicionarObra(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'addObra.html', dados)


@login_required(login_url='login/')
def adicionarNoticia(request):
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=1)}
    return render(request, 'addNoticia.html', dados)

