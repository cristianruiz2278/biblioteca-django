from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    anio_publicacion = models.PositiveIntegerField()
    autor = models.ForeignKey(
        "autores.Autor",
        on_delete=models.PROTECT,
        related_name="libros",
    )

    def __str__(self):
        return self.titulo