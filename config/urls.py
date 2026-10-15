from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from autores.views import AutorViewSet
from libros.views import LibroViewSet
from prestamos.views import PrestamoViewSet


# El router genera las rutas de los tres recursos.
router = DefaultRouter()
router.register("autores", AutorViewSet)
router.register("libros", LibroViewSet)
router.register("prestamos", PrestamoViewSet)


# Esta vista muestra nuestra página HTML.
def inicio(request):
    return render(request, "index.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("", inicio, name="inicio"),
]