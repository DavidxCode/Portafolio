from django.db import models

# Create your models here.
class About (models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    descripcionPerfil = models.CharField(max_length=100)
    Birthday = models.CharField(max_length=100)
    Website = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    freelance = models.CharField(max_length=100)
    photo= models.URLField
    class Meta:
        verbose_name = 'About me'
        verbose_name_plural = 'About me'

