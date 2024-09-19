from .models import *
from .serializer import *
from rest_framework import generics , status
from rest_framework.response import Response
from django.http import Http404

class OrdenesListView(generics.ListAPIView):
  queryset = OrdenesModel.objects.all()
  serializer_class = OrdenesSerializer
  
  def list(self, request, *args, **kwargs):
    response = super().list(request, *args, **kwargs)
    
    return Response({
      "message": "Listado de Ordenes",
      "data": response.data
    },status=status.HTTP_200_OK)
  
class OrdenesCreateView(generics.CreateAPIView):
  serializer_class = OrdenesSerializer
  
  def create(self, request, *args, **kwargs):
    # print(request.data)
    response = super().create(request, *args, **kwargs)
    
    return Response({
      "message": "Orden Creada Correctamente",
      "data": response.data
    },status=status.HTTP_201_CREATED)
  

class OrdenesUpdateView(generics.UpdateAPIView):
  queryset = OrdenesModel.objects.all()
  serializer_class = OrdenesSerializer
  
  def update(self, request, *args, **kwargs):
    try:
      response = super().update(request, *args, **kwargs)
      
      return Response({
        "message": "Orden Actualizada Correctamente",
        "data": response.data
      },status=status.HTTP_200_OK)
      
    except Http404:
      return Response({
        "message": "Orden no encontrada"
      },status=status.HTTP_404_NOT_FOUND)
    
class OrdenesDeleteView(generics.DestroyAPIView):
  queryset = OrdenesModel.objects.all()
  
  def destroy(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      instance.estado = False
      instance.save()
      
      serializer = self.get_serializer()
      
      return Response({
        "message": "Orden Eliminada Correctamente",
        "data": serializer.data
      },status=status.HTTP_200_OK)
    
    except Http404:
      return Response({
        "message": "Orden no encontrada"
      },status=status.HTTP_404_NOT_FOUND)
    
# VISTAS PARA TRANSACCIONES DE PAGOS

class PagosListView(generics.ListAPIView):
  queryset = PagosModel.objects.all()
  serializer_class = PagosSerializer
  
  def list(self, request, *args, **kwargs):
    response = super().list(request, *args, **kwargs)
    
    return Response({
      "message": "Listado de Pagos",
      "data": response.data
    },status=status.HTTP_200_OK)
    

  
class PagosUpdateView(generics.UpdateAPIView):
  queryset = PagosModel.objects.all()
  serializer_class = PagosSerializer
  
  def update(self, request, *args, **kwargs):
    try:
      response = super().update(request, *args, **kwargs)

      return Response({
        "message" : "Orden Actualizada Correctamente",
        "data": response.data
      },status=status.HTTP_200_OK)
      
    except Http404:
      return Response({
        "message": "Orden no encontrada"
      },status=status.HTTP_404_NOT_FOUND)
      
class PagosDeleteView(generics.DestroyAPIView):
  queryset = PagosModel.objects.all()
  
  def destroy(self, request, *args, **kwargs):
    try:
      super().destroy(request, *args, **kwargs)
      
      return Response({
        "message": "Orden Eliminada Correctamente"
      }, status=status.HTTP_200_OK)
    except Http404:
      return Response({
        "message": "Orden no encontrada"
      },status=status.HTTP_404_NOT_FOUND)