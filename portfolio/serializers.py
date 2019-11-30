from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.models import Instrument, Asset, BuyTransaction, SellTransaction, User
from django.utils.timezone import now


## RETURN READ ONLY AFTER  TESTS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class InstrumentSerializer(serializers.ModelSerializer):
    """Serializer for financial instrument"""
    # name = serializers.StringRelatedField()
    # symbol = serializers.StringRelatedField()
    slug = serializers.SlugField(read_only=True)

    # category = serializers.StringRelatedField()
    # price = serializers.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        model = Instrument
        fields = ('id', 'name', 'symbol', 'slug', 'category', 'price')
        # make id read-only
        # read_only_fields = ('id',)  # Tuple!
        # read_only_fields = '__all__',


class AssetSerializer(serializers.ModelSerializer):
    """Serializer for customer assets"""
    symbol = serializers.ReadOnlyField(source="instrument.symbol")
    category = serializers.ReadOnlyField(source="instrument.category")
    price = serializers.ReadOnlyField(source="instrument.price")
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Asset
        fields = ('id', 'symbol', 'quantity', 'category', 'value', 'price', 'slug')
        read_only_fields = '__all__',


class BuyTransactionSerializer(serializers.ModelSerializer):
    """Serializer for buy transactions"""
    symbol = serializers.ReadOnlyField(source="instrument.symbol")
    slug = serializers.SlugField(read_only=True)
    cash_balance = serializers.SerializerMethodField('cash_balance_field')
    instrument_price = serializers.SerializerMethodField('instrument_price_field')

    def instrument_price_field(self, obj):
        instrument = Instrument.objects.filter(id=obj.instrument.id).first()
        return instrument.price

    def cash_balance_field(self, obj):
        user = self.context['request'].user
        user_cash = Asset.objects.filter(owner=user).filter(instrument__name="USD").first()
        return user_cash.quantity

    class Meta:
        model = BuyTransaction
        fields = ('id', 'symbol', 'instrument', 'quantity', 'created_at', 'value', 'slug', 'cash_balance', 'instrument_price')
        ## READ ONLY!!!!!!!!!!!

    def validate(self, attrs):
        """Forbid USD to USD transactions, also check for sufficient cash balance"""
        # USD to USD check
        if str(attrs['instrument']) == "USD":
            raise ValidationError("USD to USD - invalid transaction")
        # Cash balance
        user = self.context['request'].user
        cash_on_hand = Asset.objects.filter(owner=user).filter(instrument__name="USD").first()
        transaction_value = attrs['instrument'].price * attrs['quantity']
        cash_balance = cash_on_hand.quantity - transaction_value
        if cash_balance < 0:
            raise ValidationError('You have insufficient funds to proceed with transaction.')
        return attrs


class SellTransactionSerializer(serializers.ModelSerializer):
    """Serializer for sell transactions"""
    symbol = serializers.ReadOnlyField(source="instrument.symbol")
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = SellTransaction
        fields = ('id', 'symbol', 'instrument', 'quantity', 'created_at', 'value', 'slug')

    def validate(self, attrs):
        """Forbid USD to USD transactions, also check for sufficient asset quantity to sell"""
        # USD to USD check
        if str(attrs['instrument']) == "USD":
            raise ValidationError("USD to USD - invalid transaction")
        # Sufficient asset quantity
        user = self.context['request'].user
        asset = Asset.objects.filter(owner=user).filter(instrument__name=attrs['instrument']).first()
        quantity = attrs['quantity']
        asset_balance = asset.quantity - quantity
        if asset_balance < 0:
            raise ValidationError('You have insufficient asset quantity to proceed with transaction.')
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ## CASH BALANCE!!!!!!!!!!
        fields = ["email"]
