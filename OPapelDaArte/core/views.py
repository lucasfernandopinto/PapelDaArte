from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from core.models import Artista, Obras, Noticia
import random


# Create your views here.

def index(request):
    aux = Noticia.objects.random()

    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id),
             'obras': [Obras.objects.random(), Obras.objects.random(), Obras.objects.random()]}
    return render(request, 'index.html', dados)


def teste(request):
    return render(request, 'teste.html')


def buscaArtistas(request):
    busca = request.GET.get('busca', None)
    artistas = Artista.objects.filter(art_sobrenome__startswith=busca)
    resultado = ''
    if artistas:
        aux = 0
        for artista in artistas:
            aux += 1
            resultado += '<a href="/Artistas/{}" class="list-group-item list-group-item-action">{}, {}</a>'.format(artista.art_sobrenome, artista.art_sobrenome, artista.art_nome)
            print(resultado)
            if aux == 10:
                break
    else:
        resultado = "<br><center><h6>Sem resultados!</h6></center>"
    dados = {'conteudo': resultado}
    return JsonResponse(dados)


def artista(request, art_sobrenome):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'artistaPrincipal': Artista.objects.filter(art_sobrenome=art_sobrenome),
             'obras': Obras.objects.filter(obr_artista__in=Artista.objects.filter(art_sobrenome=art_sobrenome)),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'artista.html', dados)


def julioReis(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'julioReis.html', dados)


def oPapelDaArte(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'oPapelDaArte.html', dados)


def historiaGravura(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'historiaGravura.html', dados)


def tecnicasImpressao(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'tecnicasImpressao.html', dados)


def emolduramento(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'emolduramento.html', dados)


def noticias(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'noticias.html', dados)


def artigos(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'artigos.html', dados)


def entrevistas(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'entrevistas.html', dados)


def historiaSeculo19(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'seculo19.html', dados)


def historiaBrasil(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'brasil.html', dados)


def aguaForte(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'aguaForte.html', dados)


def aguaTinta(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'aguaTinta.html', dados)


def buril(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'buril.html', dados)


def heliogravura(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'heliogravura.html', dados)


def linoleo(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'linoleo.html', dados)


def litografia(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'litografica.html', dados)


def maneiraNegra(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'maneiraNegra.html', dados)


def pontaSeca(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'pontaSeca.html', dados)


def processoAcucar(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'processoAcucar.html', dados)


def processoEnxofre(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'processoEnxofre.html', dados)


def processoLavis(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'processoLavis.html', dados)


def processoRelevo(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'processoRelevo.html', dados)


def serigrafia(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'serigrafia.html', dados)


def vernizMole(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'vernizMole.html', dados)


def xilogravura(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'xilogravura.html', dados)


@login_required(login_url='login/')
def adicionarArtista(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'addArtista.html', dados)


@login_required(login_url='login/')
def adicionarObra(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'addObra.html', dados)


@login_required(login_url='login/')
def adicionarNoticia(request):
    aux = Noticia.objects.random()
    dados = {'artista': Artista.objects.all(),
             'noticia': Noticia.objects.filter(id=aux.id)}
    return render(request, 'addNoticia.html', dados)

