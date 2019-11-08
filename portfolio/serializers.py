from rest_framework import serializers

from core.models import Instrument

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