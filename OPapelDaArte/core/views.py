from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from core.models import Artista, Obra, Noticia
import random


# Create your views here.

def index(request):
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             'obras': [Obra.objects.random(), Obra.objects.random(), Obra.objects.random()],
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt}
    return render(request, 'index.html', dados)


def teste(request):
    return render(request, 'teste.html')


def buscaArtistas(request):
    busca = request.GET.get('busca', None)
    artistas = Artista.objects.filter(art_nome__startswith=busca)
    if busca == '':
        artistas = Artista.objects.all()[0:15]
    resultado = ''
    if artistas:
        aux = 0
        for artista in artistas:
            aux += 1
            resultado += '<a href="/Artistas/{}" class="list-group-item list-group-item-action">{}</a>'.format(artista.art_nome, artista.art_nome)
            if aux == 15:
                break
    else:
        resultado = "<br><center><h6>Sem resultados!</h6></center>"
    dados = {'conteudo': resultado}
    return JsonResponse(dados)


def artista(request, art_nome):
    #aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             'artistaPrincipal': Artista.objects.filter(art_nome=art_nome),
             'obras': Obra.objects.filter(obr_artista__in=Artista.objects.filter(art_nome=art_nome)),
             #'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'artista.html', dados)


def julioReis(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'julioReis.html', dados)


def oPapelDaArte(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'oPapelDaArte.html', dados)


def historiaGravura(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'historiaGravura.html', dados)


def tecnicasImpressao(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'tecnicasImpressao.html', dados)


def emolduramento(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'emolduramento.html', dados)


def noticias(request):
    # aux = Noticia.objects.random()
    busca = request.GET.get('b', None)
    auxBusca = 0
    paginaArt = 0
    nPaginasArt = 0
    pagina = 0
    nPaginas = 0
    if (busca):
        auxBusca = 1
        resultado = Noticia.objects.filter(not_nome__contains=busca)
        if not resultado:
            auxBusca = 2
    else:
        paginaArt = request.GET.get('pa', None)
        nPaginasArt = len(Artista.objects.all()) / 15
        nPaginasArt = round(nPaginasArt + 0.46)
        pagina = request.GET.get('p', None)
        nPaginas = len(Noticia.objects.all()) / 4
        nPaginas = round(nPaginas+0.4)
        if (pagina):
            try:
                pagina = int(pagina)
            except:
                pagina = 1
        else:
            pagina = 1
        offset = 0
        limit = 0
        if (pagina > 1):
            offset = (pagina - 1) * 4
            limit = pagina * 4
        else:
            offset = 0
            limit = 4
        resultado = Noticia.objects.all().order_by('-not_publi')[offset:limit]
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    ordem = request.GET.get('ordenar_por', None)
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    resultadoArt = Artista.objects.all().order_by('art_nome')[offsetArt:limitArt]
    dados = {'artista': resultadoArt,
             #'noticia': Noticia.objects.filter(id=aux.id)
             'noticias': resultado,
             'nPaginas': nPaginas,
             'paginaAtual': pagina,
             'auxBusca': auxBusca,
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt}
    return render(request, 'noticias.html', dados)


def artigos(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    pagina = request.GET.get('p', None)
    nPaginas = len(Noticia.objects.filter(not_tipo='A')) / 4
    nPaginas = round(nPaginas+0.4)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    if (pagina):
        try:
            pagina = int(pagina)
        except:
            pagina = 1
    else:
        pagina = 1
    ordem = request.GET.get('ordenar_por', None)
    offsetArt = 0
    limitArt = 0
    offset = 0
    limit = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    if (pagina > 1):
        offset = (pagina - 1) * 4
        limit = pagina * 4
    else:
        pagina = 1
        offset = 0
        limit = 4
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             #'noticia': Noticia.objects.filter(id=aux.id)
             'noticias': Noticia.objects.filter(not_tipo='A').order_by('-not_publi')[offset:limit],
             'nPaginas': nPaginas,
             'paginaAtual': pagina,
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt}
    return render(request, 'artigos.html', dados)


def entrevistas(request):
    #aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    pagina = request.GET.get('p', None)
    nPaginas = len(Noticia.objects.filter(not_tipo='E')) / 4
    nPaginas = round(nPaginas+0.4)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    if (pagina):
        try:
            pagina = int(pagina)
        except:
            pagina = 1
    else:
        pagina = 1
    ordem = request.GET.get('ordenar_por', None)
    offsetArt = 0
    limitArt = 0
    offset = 0
    limit = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    if (pagina > 1):
        offset = (pagina - 1) * 4
        limit = pagina * 4
    else:
        offset = 0
        limit = 4
    if (ordem == 'data'):
        resultado = Noticia.objects.filter(not_tipo='E').order_by(ordem)[offset:limit]
    elif ( ordem == 'data_desc'):
        pass
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             #'noticia': Noticia.objects.filter(id=aux.id)
             'noticias': Noticia.objects.filter(not_tipo='E').order_by('-not_publi')[offset:limit],
             'nPaginas': nPaginas,
             'paginaAtual': pagina,
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt}
    return render(request, 'entrevistas.html', dados)


def verNoticia(request, id):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt,
             'noticia': Noticia.objects.filter(id=id)}
    return render(request, 'noticia.html', dados)


def historiaSeculo19(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'seculo19.html', dados)


def historiaBrasil(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'brasil.html', dados)


def aguaForte(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'aguaForte.html', dados)


def aguaTinta(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'aguaTinta.html', dados)


def buril(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'buril.html', dados)


def heliogravura(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'heliogravura.html', dados)


def linoleo(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'linoleo.html', dados)


def litografia(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'litografica.html', dados)


def maneiraNegra(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'maneiraNegra.html', dados)


def pontaSeca(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'pontaSeca.html', dados)


def processoAcucar(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'processoAcucar.html', dados)


def processoEnxofre(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'processoEnxofre.html', dados)


def processoLavis(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'processoLavis.html', dados)


def processoRelevo(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'processoRelevo.html', dados)


def serigrafia(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'serigrafia.html', dados)


def vernizMole(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
    return render(request, 'vernizMole.html', dados)


def xilogravura(request):
    # aux = Noticia.objects.random()
    paginaArt = request.GET.get('pa', None)
    nPaginasArt = len(Artista.objects.all()) / 15
    nPaginasArt = round(nPaginasArt + 0.46)
    if (nPaginasArt):
        try:
            paginaArt = int(paginaArt)
        except:
            paginaArt = 1
    else:
        paginaArt = 1
    offsetArt = 0
    limitArt = 0
    if (paginaArt > 1):
        offsetArt = (paginaArt - 1) * 15
        limitArt = paginaArt * 15
    else:
        paginaArt = 1
        offsetArt = 0
        limitArt = 15
    dados = {'artista': Artista.objects.all().order_by('art_nome')[offsetArt:limitArt],
             # 'noticia': Noticia.objects.filter(id=aux.id)
             'nPaginasArt': nPaginasArt,
             'paginaAtualArt': paginaArt
             }
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

