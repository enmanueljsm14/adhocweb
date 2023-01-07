from adhocwep.settings import MEDIA_URL, STATIC_URL
from django.db import models
from datetime import datetime
# Create your models here.

class portafolio(models.Model):
    id_portafolio = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    titulo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=2500)
    fecha = models.DateField(default=datetime.now)
    imagen = models.ImageField(upload_to='portafolio/%Y/%m/%d', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    estado=models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["id_portafolio"]
        verbose_name = "Portafolio"
        verbose_name_plural = "Portafolios"

    def get_img_portafolio(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

class about(models.Model):
    id_about = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    titulo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=2500)
    imagen= models.ImageField(upload_to='about/%Y/%m/%d', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    estado=models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["id_about"]
        verbose_name = "Quienes somos"
        verbose_name_plural = "Quienes somos"

    def get_img_about(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')


class feature(models.Model):
    id_feature = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    titulo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=2500)
    icono = models.CharField(max_length=250)
    imagen= models.ImageField(upload_to='feature/%Y/%m/%d', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    estado=models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["id_feature"]
        verbose_name = "Caracteristica"
        verbose_name_plural = "Caracteristicas"

    def get_img_feature(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

class servicios(models.Model):
    id_servicios = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    titulo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=2500)
    icono = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    estado=models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["id_servicios"]
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"


class contact(models.Model):
    id_contact = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    nombre = models.CharField(max_length=250)
    correo = models.CharField(max_length=250)
    asunto = models.CharField(max_length=2500)
    mensaje = models.CharField(max_length=25000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    estado=models.BooleanField(default=True)

    def __str__(self):
        return self.asunto

    class Meta:
        ordering = ["id_contact"]
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

