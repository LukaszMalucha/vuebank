from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.models import Instrument, Asset, BuyTransaction, SellTransaction, User
from django.utils.timezone import now


class InstrumentSerializer(serializers.ModelSerializer):
    """Serializer for financial instrument"""
    slug = serializers.SlugField(read_only=True)
    cash_balance = serializers.SerializerMethodField('cash_balance_field')
    user_holdings = serializers.SerializerMethodField('user_holdings_field')

    def user_holdings_field(self, obj):
        user = self.context['request'].user
        user_holdings = Asset.objects.filter(owner=user).filter(instrument__name=obj.name).first()
        if user_holdings:
            return user_holdings.quantity
        else:
            return 0

    def cash_balance_field(self, obj):
        user = self.context['request'].user
        user_cash = Asset.objects.filter(owner=user).filter(instrument__name="USD").first()
        return user_cash.quantity

    class Meta:
        model = Instrument
        fields = ('id', 'name', 'symbol', 'slug', 'category', 'price', 'cash_balance', 'user_holdings')
        read_only_fields = '__all__',


class AssetSerializer(serializers.ModelSerializer):
    """Serializer for customer assets"""
    name = serializers.ReadOnlyField(source="instrument.name")
    symbol = serializers.ReadOnlyField(source="instrument.symbol")
    category = serializers.ReadOnlyField(source="instrument.category")
    price = serializers.ReadOnlyField(source="instrument.price")
    instrument_slug = serializers.ReadOnlyField(source="instrument.slug")
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Asset
        fields = ('id', 'name', 'symbol', 'instrument_slug', 'quantity', 'category', 'value', 'price', 'slug')
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
        fields = ('id', 'symbol', 'instrument', 'quantity', 'created_at',
                  'value', 'slug', 'cash_balance', 'instrument_price')
        read_only_fields = ('id', 'symbol', 'cash_balance', 'instrument_price')

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
        read_only_fields = ('id', 'symbol', 'cash_balance', 'instrument_price')

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
    """For request.user logic in Vue.js frontend"""

    class Meta:
        model = User
        fields = ["email"]
