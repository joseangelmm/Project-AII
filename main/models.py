from django.db import models

class Usuario(models.Model):
    idUsuario =                                                models.AutoField(primary_key=True)
    nombre =                                                   models.CharField(max_length=100)
    password=                                                  models.CharField(max_length=100)
    edad =                                                     models.IntegerField(verbose_name='Edad', help_text='Debe introducir una edad')
    sexo =                                                     models.CharField(max_length=1, verbose_name='Sexo', help_text='Debe elegir entre M o F')
    codigoPostal =                                             models.TextField(verbose_name='Codigo Postal')
    
    numerosDeNoticiasBuscadasDeLaCategoriaCultura =            models.IntegerField()
    numerosDeNoticiasBuscadasDeLaCategoriaTecnologiaYCiencia = models.IntegerField()
    numerosDeNoticiasBuscadasDeLaCategoriaInternacional =      models.IntegerField()
    numerosDeNoticiasBuscadasDeLaCategoriaPolitica =           models.IntegerField()
    
    def __str__(self):
        return self.idUsuario
    
class Noticia(models.Model):
    idNoticia =                                                models.AutoField(primary_key=True)
    titulo =                                                   models.TextField(verbose_name='Titulo')
    fecha =                                                    models.DateField(verbose_name='Fecha', null=True)
    #fecha =                                                    models.TextField(verbose_name='Fecha', null=True)
    autor =                                                    models.TextField(verbose_name='autor')
    link  =                                                    models.TextField(verbose_name='link')
    categoria =                                                models.TextField()
    imagen =                                                   models.TextField()
    def __str__(self):
        return self.titulo
   
    