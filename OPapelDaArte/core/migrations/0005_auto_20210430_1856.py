# Generated by Django 3.2 on 2021-04-30 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210419_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='not_publi',
            field=models.DateField(auto_now=True, verbose_name='Data de publicação'),
        ),
        migrations.AlterField(
            model_name='artista',
            name='art_desc',
            field=models.TextField(blank=True, null=True, verbose_name='Texto descritivo:'),
        ),
        migrations.AlterField(
            model_name='artista',
            name='art_imagem',
            field=models.ImageField(upload_to='Artistas', verbose_name='Imagem do artista:'),
        ),
        migrations.AlterField(
            model_name='artista',
            name='art_morte',
            field=models.IntegerField(null=True, verbose_name='Ano de falecimento'),
        ),
        migrations.AlterField(
            model_name='artista',
            name='art_nascimento',
            field=models.IntegerField(null=True, verbose_name='Ano de nascimento'),
        ),
        migrations.AlterField(
            model_name='artista',
            name='art_nome',
            field=models.CharField(max_length=100, verbose_name='Nome do artista'),
        ),
        migrations.AlterField(
            model_name='artista',
            name='art_sobrenome',
            field=models.CharField(max_length=100, verbose_name='Sobrenome do artista:'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='not_desc',
            field=models.TextField(verbose_name='Faça a descrição da sua publicação:'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='not_imagem',
            field=models.ImageField(upload_to='Artigos', verbose_name='Selecione a imagem da publicação:'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='not_nome',
            field=models.CharField(max_length=100, verbose_name='Nome da publicação:'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='not_tipo',
            field=models.CharField(choices=[('N', 'Notícia'), ('A', 'Artigo'), ('E', 'Entrevista')], max_length=1, verbose_name='Selecione o tipo de publicação que deseja fazer:'),
        ),
        migrations.AlterField(
            model_name='obras',
            name='obr_ano',
            field=models.IntegerField(null=True, verbose_name='Ano de publicação:'),
        ),
        migrations.AlterField(
            model_name='obras',
            name='obr_artista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.artista', verbose_name='Artista:'),
        ),
        migrations.AlterField(
            model_name='obras',
            name='obr_img',
            field=models.ImageField(upload_to='Obras', verbose_name='Selecione a obra:'),
        ),
        migrations.AlterField(
            model_name='obras',
            name='obr_info',
            field=models.TextField(null=True, verbose_name='Adicione as informações adicionais da obra:'),
        ),
        migrations.AlterField(
            model_name='obras',
            name='obr_legenda',
            field=models.CharField(max_length=200, null=True, verbose_name='Legenda da obra'),
        ),
        migrations.AlterField(
            model_name='obras',
            name='obr_nome',
            field=models.CharField(max_length=200, verbose_name='Nome da obra:'),
        ),
        migrations.AlterField(
            model_name='obras',
            name='obr_status',
            field=models.CharField(choices=[('D', 'Disponível'), ('V', 'Vendida')], max_length=50, null=True, verbose_name='Estado da obra:'),
        ),
        migrations.AlterField(
            model_name='obras',
            name='obr_valor',
            field=models.FloatField(null=True, verbose_name='Valor da obra:'),
        ),
    ]