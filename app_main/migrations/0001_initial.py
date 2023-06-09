# Generated by Django 4.1.7 on 2023-03-29 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emprendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(help_text='Introduce tu nombre completo', max_length=200)),
                ('nit', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('banco', models.CharField(max_length=20)),
                ('img_perfil', models.ImageField(default='default.png', upload_to='')),
                ('direccion', models.CharField(max_length=100)),
                ('rubro', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('password1', models.CharField(max_length=10)),
                ('password2', models.CharField(max_length=10)),
            ],
        ),
    ]
