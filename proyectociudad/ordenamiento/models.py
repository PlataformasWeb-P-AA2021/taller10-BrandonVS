from django.db import models


# Create your models here.

class Parroquia(models.Model):
    class Meta:
        ordering = ["tipo_parroquia"]
        verbose_name_plural = "Parroquias"

    opciones_tipo_parroquia = (
        ('urbana', 'Parroquia Urbana'),
        ('rural', 'Parroquia Rural'),
    )

    nombre = models.CharField(max_length=30)
    tipo_parroquia = models.CharField(max_length=30, choices=opciones_tipo_parroquia)

    def __str__(self):
        return "%s - Tipo de parroquia: %s" % (self.nombre,
                                               self.tipo_parroquia)


class Barrio(models.Model):
    class Meta:
        ordering = ["numero_parques"]
        verbose_name_plural = "Barrios"

    opciones_numero_parques = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
    )

    nombre = models.CharField(max_length=30)
    numero_viviendas = models.IntegerField()
    numero_parques = models.IntegerField(choices=opciones_numero_parques)
    numero_edificios = models.IntegerField()
    parroquia = models.ForeignKey(Parroquia, related_name='losbarrios', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - Viviendas: %d - Parques: %d - Edificios: %d - Parroquia: %s" % (self.nombre,
                                                                                     self.numero_viviendas,
                                                                                     self.numero_parques,
                                                                                     self.numero_edificios,
                                                                                     self.parroquia)
