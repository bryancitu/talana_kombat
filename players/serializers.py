from rest_framework import serializers
from .models import Power, Player

class PowersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Power
        fields = ['id', 'name', 'combination', 'energy', 'player']

class PlayersSerializer(serializers.ModelSerializer):
    power = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = ['id', 'full_name', 'username', 'power']

    def get_power(self,obj):
        player = Player.objects.filter(full_name=obj).first()
        powers = Power.objects.filter(player__id=player.id)
        serializer = PowersSerializer(powers, many=True)
        return serializer.data
