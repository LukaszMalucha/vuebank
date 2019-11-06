from rest_framework import serializers

from core.models import Instrument


class InstrumentSerializer(serializers.ModelSerializer):
    """Serializer for financial instrument"""
    name = serializers.StringRelatedField(read_only=True)
    symbol = serializers.StringRelatedField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    price = serializers.DecimalField(max_digits=19, decimal_places=2, read_only=True)

    class Meta:
        model = Instrument
        fields = ('id', 'name', 'symbol', 'category', 'price')
        # make id read-only
        read_only_fields = ('id',)  # Tuple!
