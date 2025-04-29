from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from TrackingShipment.models import Shipment, ShipmentUpdate
from .serializers import ShipmentSerializer, ShipmentUpdateSerializer
from .permissions import IsAdminOrReadOnly

class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def search(self, request):
        tracking_number = request.query_params.get('tracking_number')
        if not tracking_number:
            return Response({'error': 'tracking_number est requis'}, status=status.HTTP_400_BAD_REQUEST)

        shipment = Shipment.objects.filter(tracking_number=tracking_number).first()
        if shipment:
            serializer = self.get_serializer(shipment)
            return Response(serializer.data)
        return Response({'error': 'Colis non trouvé'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def add_update(self, request, pk=None):
        shipment = self.get_object()
        serializer = ShipmentUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(shipment=shipment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['patch'], permission_classes=[AllowAny])
    def mark_delivered(self, request, pk=None):
        shipment = self.get_object()
        shipment.status = 'DELIVERED'
        shipment.save()
        return Response({'message': 'Statut mis à jour comme livré.'}, status=status.HTTP_200_OK)
