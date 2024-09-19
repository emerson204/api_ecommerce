from .models import *
from rest_framework import serializers

class OrdenDetalleSerializer(serializers.ModelSerializer):
  orden_id = serializers.IntegerField(read_only=True)
  class Meta:
    model = OrdenDetailModel
    fields = "__all__"

class OrdenesSerializer(serializers.ModelSerializer):
  
  details = OrdenDetalleSerializer(many=True, source="orden_detail")
  
  class Meta:
    model = OrdenesModel
    fields = "__all__"  

class PagosSerializer(serializers.ModelSerializer):
  class Meta:
    model = PagosModel
    fields = "__all__"