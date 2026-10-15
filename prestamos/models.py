from django.db import models

class Prestamo(models.Model):
    nombre_lector = models.CharField(max_length=100)
    fecha_prestamo = models.DateField()
    libro = models.ForeignKey(
        "libros.Libro",
        on_delete=models.PROTECT,
        related_name="prestamos",
    )

    def __str__(self):
        return f"{self.nombre_lector} - {self.libro}"