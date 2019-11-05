from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsAdminOrReadOnly
from core.models import Instrument

from portfolio import serializers


class InstrumentViewSet(viewsets.ModelViewSet):
    """Create instruments in the database"""
    # permission_classes = (IsAuthenticated, IsAdminOrReadOnly)
    serializer_class = serializers.InstrumentSerializer
    queryset = Instrument.objects.all()

    def get_queryset(self):
        """Display all instruments"""
        queryset = self.queryset
        return queryset.order_by('-name')

    def perform_create(self, serializer):
        """Create a new financial instrument"""
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





