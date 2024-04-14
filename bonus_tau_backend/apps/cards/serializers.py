from rest_framework import serializers

from .models import Card


class CardCreateSerializer(serializers.ModelSerializer):
    """Card Creation Serializer."""

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    usage_date = serializers.DateField(input_formats=['%m/%y'])
    

    class Meta: 
        model = Card
        fields = (
            'id',
            'bank_title',
            'card_type',
            'number',
            'usage_date',
            'owner'
        )

    def create(self, validated_data):
        card = Card.objects.create(**validated_data)

        return card
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['usage_date'] = instance.usage_date.strftime('%m/%Y')
        return data
    

class CardSerializer(serializers.ModelSerializer):
    """Serializer for Card model."""

    class Meta:
        model = Card
        fields = (
            'id', 
            'bank_title', 
            'card_type', 
            'number', 
            'usage_date'
        )
