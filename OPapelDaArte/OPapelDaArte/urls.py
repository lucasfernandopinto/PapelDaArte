"""OPapelDaArte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('Artistas/<art_sobrenome>', views.artista),
    path('Julio-Reis', views.julioReis),
    path('O-Papel-da-Arte', views.oPapelDaArte),
    path('Historia-da-Gravura', views.historiaGravura),
    path('Tecnicas-de-Impressao', views.tecnicasImpressao),
    path('Emolduramento-e-Restauracao', views.emolduramento),
    path('Noticias', views.noticias),
    path('Artigos', views.artigos),
    path('Entrevistas', views.entrevistas),
    path('Adicionar-Artista', views.adicionarArtista),
    path('Artistas/<art_sobrenome>/Obras/Adicionar-Obra', views.adicionarObra),
    path('Historia-da-Gravura/Seculo-19', views.historiaSeculo19),
    path('Historia-da-Gravura/Brasil', views.historiaBrasil),
    path('Tecnicas-de-Impressao/Agua-Forte', views.aguaForte),
    path('Tecnicas-de-Impressao/Agua-Tinta', views.aguaTinta),
    path('Tecnicas-de-Impressao/Buril', views.buril),
    path('Tecnicas-de-Impressao/Heliogravura', views.heliogravura),
    path('Tecnicas-de-Impressao/Linoleo', views.linoleo),
    path('Tecnicas-de-Impressao/Litografia', views.litografia),
    path('Tecnicas-de-Impressao/Maneira-Negra', views.maneiraNegra),
    path('Tecnicas-de-Impressao/Ponta-Seca', views.pontaSeca),
    path('Tecnicas-de-Impressao/Processo-do-Acucar', views.processoAcucar),
    path('Tecnicas-de-Impressao/Processo-do-Enxofre', views.processoEnxofre),
    path('Tecnicas-de-Impressao/Processo-do-Lavis', views.processoLavis),
    path('Tecnicas-de-Impressao/Processo-do-Relevo', views.processoRelevo),
    path('Tecnicas-de-Impressao/Serigrafia', views.serigrafia),
    path('Tecnicas-de-Impressao/Verniz-Mole', views.vernizMole),
    path('Tecnicas-de-Impressao/Xilogravura', views.xilogravura),
]

admin.site.site_header = 'Administração O Papel da Arte'
admin.site.index_title = 'Registros do Site'
