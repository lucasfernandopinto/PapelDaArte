# Generated by Django 3.1.5 on 2021-02-21 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_nome', models.CharField(max_length=100)),
                ('art_sobrenome', models.CharField(max_length=100)),
                ('art_imagem', models.CharField(max_length=80)),
                ('art_desc', models.TextField(blank=True, null=True)),
                ('art_nascimento', models.IntegerField(null=True)),
                ('art_morte', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'artista',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('not_nome', models.CharField(max_length=100)),
                ('not_tipo', models.CharField(max_length=15)),
                ('not_desc', models.TextField()),
                ('not_imagem', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'noticias',
            },
        ),
        migrations.CreateModel(
            name='Obras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obr_img', models.CharField(max_length=100)),
                ('obr_legenda', models.CharField(max_length=200, null=True)),
                ('obr_nome', models.CharField(max_length=200)),
                ('obr_ano', models.IntegerField(null=True)),
                ('obr_valor', models.FloatField(null=True)),
                ('obr_status', models.CharField(max_length=50, null=True)),
                ('obr_info', models.TextField(null=True)),
                ('obr_artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.artista')),
            ],
            options={
                'db_table': 'obras',
            },
        ),
    ]