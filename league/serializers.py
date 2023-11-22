from league.models import Season
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    season = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Season.objects.all())

    class Meta:
        model = User
        fields = "__all__"


class SeasonSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.email")

    #
    class Meta:
        model = Season
        fields = ["created_on",
                  "season",
                  "winner",
                  "second",
                  "third",
                  "fourth",
                  "first_relegated",
                  "second_relegated",
                  "third_relegated",
                  "owner"]


class SeasonDeserializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = [
            "id",
            "created_on",
            "season",
        ]
