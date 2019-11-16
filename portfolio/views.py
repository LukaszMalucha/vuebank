from rest_framework.response import Response
from rest_framework import generics, viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from core.permissions import IsAdminOrReadOnly
from core.models import Instrument, Asset, BuyTransaction, SellTransaction

from portfolio import serializers


class BaseRestrictedViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Basic authentication and permission"""
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)


class InstrumentViewSet(viewsets.ModelViewSet):
    """Create instruments in the database"""
    # permission_classes = (IsAuthenticated, IsAdminOrReadOnly)
    serializer_class = serializers.InstrumentSerializer
    queryset = Instrument.objects.all()
    lookup_field = "slug"

    def get_queryset(self):
        """Display all instruments"""
        queryset = self.queryset
        return queryset.order_by('-name')

    def perform_create(self, serializer):
        """Create a new financial instrument"""
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssetManagerViewSet(viewsets.ViewSet):
    """Customer's asset view"""
    # authentication_classes = (TokenAuthentication, )
    # permisssion_classes = (IsAuthenticated, )
    serializer_class = serializers.AssetSerializer
    queryset = Asset.objects.all()

    def list(self, request):
        queryset = Asset.objects.filter(owner=self.request.user)
        serializer = serializers.AssetSerializer(queryset, many=True)
        return Response(serializer.data)


class CashBalanceViewSet(BaseRestrictedViewSet):
    """Cash balance view with top-up functrionality"""
    serializer_class = serializers.AssetSerializer
    queryset = Asset.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(owner=self.request.user).filter(instument__name="USD")

    def post(self, request):
        cash_serializer = serializers.AssetSerializer(data=request.data)
        cash_balance = Asset.objects.get(instrument__name="USD", owner=request.user)
        if cash_serializer.is_valid():
            top_up = int(request.data['quantity'])
            cash_balance.quantity += top_up
            cash_balance.save()
            return Response(f"You've successfully transferred {top_up} $ to your Account."
                            f" Your current cash balance is {cash_balance.quantity}$.")

        return Response(cash_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellAssetViewSet(BaseRestrictedViewSet, mixins.CreateModelMixin):
    """Sell asset transaction view"""
    serializer_class = serializers.SellTransactionSerializer
    queryset = SellTransaction.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """Sell financial instrument"""
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class BuyAssetCreateAPIView(generics.CreateAPIView):
    """Buy asset transaction view"""
    queryset = BuyTransaction.objects.all()
    serializer_class = serializers.BuyTransactionSerializer

    def perform_create(self, serializer):
        """Create a new financial instrument"""
        cash_on_hand = Asset.objects.filter(owner=self.request.user).filter(instrument__name="USD").first()
        instrument = Instrument.objects.filter(symbol=serializer.data['symbol']).first()
        quantity = serializer.data['quantity']
        transaction_value = instrument.price * quantity
        cash_balance = cash_on_hand.quantity - transaction_value
        if cash_balance < 0:
            raise ValidationError(str(cash_balance))
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuyAssetListAPIView(generics.ListAPIView):
    """Buy Transactions list view"""
    serializer_class = serializers.BuyTransactionSerializer

    def get_queryset(self):
        return BuyTransaction.objects.filter(owner=self.request.user).order_by("-created_at")