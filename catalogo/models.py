from __future__ import annotations

from django.db import models
from django.utils import timezone


class Autor(models.Model):
    """
    Representa a un autor/a.
    Requerido: nombre, email único, biografía opcional.
    """
    nombre = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    biografia= models.TextField(blank=True)

    # TODO: implementar los campos del modelo
    # Ejemplo de campo:
    # nombre = models.CharField(max_length=120)
    #
    # nombre   → CharField (max_length a elección)
    # email    → EmailField (unique=True)
    # biografia → TextField (blank=True para hacerlo opcional)

    pass

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    """
    Categoría temática de libros.
    Ejemplos: 'fantasía', 'ciencia ficción', 'historia'.
    """

    # TODO: implementar el campo nombre (unique=True)
    nombre= models.CharField(max_length=20,unique=True)
    pass

    def __str__(self) -> str:
        return self.nombre


class Libro(models.Model):
    """
    Libro del catálogo de la biblioteca.
    Tiene relación N:1 con Autor y N:M con Categoria.
    """

    # TODO: implementar los campos:
    # titulo          → CharField
    # isbn            → CharField (unique=True)
    # fecha_publicacion → DateField
    # cantidad_total  → PositiveIntegerField
    # autor           → ForeignKey(Autor, on_delete=models.PROTECT)
    # categorias      → ManyToManyField(Categoria)
    #
    # Preguntas guía:
    # ¿Qué pasa si eliminás un autor que tiene libros? (PROTECT vs CASCADE)
    # ¿Por qué isbn debe ser único?

    titulo            = models.CharField(max_length=200)
    isbn              = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    cantidad_total    = models.PositiveIntegerField()
    autor             = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name='libros')
    categorias        = models.ManyToManyField(Categoria, blank=True)



    pass

