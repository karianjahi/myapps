from rest_framework import serializers
from directions.models import Direction


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ["id", "created_on", "origin", "destination", "distance", "duration",]
