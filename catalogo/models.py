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

    

    def __str__(self):
        return self.nombre
    
    pass

class Categoria(models.Model):
    """
    Categoría temática de libros.
    Ejemplos: 'fantasía', 'ciencia ficción', 'historia'.
    """

    # TODO: implementar el campo nombre (unique=True)
    nombre= models.CharField(max_length=20,unique=True)
    

    def __str__(self) -> str:
        return self.nombre
    pass

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
    isbn              = models.CharField(max_length=30, unique=True)
    fecha_publicacion = models.DateField()
    cantidad_total    = models.PositiveIntegerField()
    autor             = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name='libros')
    categorias        = models.ManyToManyField(Categoria, blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.isbn})"

    def prestamos_activos(self) -> int:
        return self.prestamos.filter(fecha_devolucion__isnull=True).count()

    def disponibles(self) -> int:
        return self.cantidad_total - self.prestamos_activos()

    def tiene_disponibles(self) -> bool:
        return self.disponibles() > 0

    pass

class Prestamo(models.Model):
    """
    Registro de un préstamo de libro a un usuario.
    Si fecha_devolucion es NULL → el préstamo está activo.
    """
    libro              = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos')
    nombre_prestatario = models.CharField(max_length=100)
    fecha_prestamo     = models.DateField(default=timezone.now)
    fecha_devolucion   = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.libro.titulo} → {self.nombre_prestatario}"
    pass