from rest_framework import serializers
from TrackingShipment.models import Shipment, ShipmentUpdate

class ShipmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentUpdate
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    updates = ShipmentUpdateSerializer(many=True, read_only=True)
    
    class Meta:
        model = Shipment
        fields = '__all__'
