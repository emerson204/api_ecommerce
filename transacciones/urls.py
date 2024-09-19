from django.urls import path
from .views import *

urlpatterns = [
  path("list/ordenes/", OrdenesListView.as_view()),
  path("create/ordenes/", OrdenesCreateView.as_view()),
  path("update/ordenes/<int:pk>", OrdenesUpdateView.as_view()),
  path("delete/ordenes/<int:pk>", OrdenesDeleteView.as_view()),
]
