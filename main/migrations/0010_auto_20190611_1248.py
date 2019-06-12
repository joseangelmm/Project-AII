# Generated by Django 2.2 on 2019-06-11 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_auto_20190610_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='gustosUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerosDeNoticiasBuscadasDeLaCategoriaCultura', models.IntegerField()),
                ('numerosDeNoticiasBuscadasDeLaCategoriaTecnologiaYCiencia', models.IntegerField()),
                ('numerosDeNoticiasBuscadasDeLaCategoriaInternacional', models.IntegerField()),
                ('numerosDeNoticiasBuscadasDeLaCategoriaPolitica', models.IntegerField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
