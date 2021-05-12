from django.contrib import admin
from core.models import Artista, Obra, Noticia

# Register your models here.

class artistaAdmin(admin.ModelAdmin):
    list_display = ('art_nome',)
    search_fields = ['art_nome', ]

class obraAdmin(admin.ModelAdmin):
    list_display = ('obr_nome', 'obr_ano', 'obr_status', 'obr_artista')
    list_filter = ('obr_status', 'obr_artista')
    search_fields = ['obr_nome',]
    actions = ['mudarParaVendida']

    @admin.action(description='Marcar obras seleciondas como vendidas')
    def mudarParaVendida(self, request, queryset):
        queryset.update(obr_status='V')

    list_per_page = 20

class noticiaAdmin(admin.ModelAdmin):
    list_display = ('not_nome', 'not_publi', 'not_tipo')
    list_filter = ('not_tipo', 'not_publi')
    search_fields = ['not_nome',]

admin.site.register(Artista, artistaAdmin)
admin.site.register(Obra, obraAdmin)
admin.site.register(Noticia, noticiaAdmin)
