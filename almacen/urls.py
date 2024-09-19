from django.urls import path
from .views import * 

urlpatterns = [
  # Urls de categorias
  path("list/categorias/", CategoriasListView.as_view()),
  path("create/categorias/", CategoriasCreateView.as_view()),
  path("update/categorias/<int:pk>", CategoriasUpdateView.as_view()),
  path("delete/categorias/<int:pk>", CategoriasDeleteView.as_view()),
  
  # Urls de productos
  path("list/productos/", ProductosListView.as_view()),
  path("create/productos/", ProductosCreateView.as_view()),
  path("update/productos/<int:pk>", ProductosUpdateView.as_view()),
  path("delete/productos/<int:pk>", ProductosDeleteView.as_view()),
  
  # Urls de direcciones
  path("list/direcciones/", DireccionesListView.as_view()),
  path("create/direcciones/", DireccionesCreateView.as_view()),
  path("update/direcciones/<int:pk>", DireccionesUpdateView.as_view()),
  path("delete/direcciones/<int:pk>", DireccionesDeleteView.as_view()),
]
    
