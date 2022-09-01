from rest_framework import serializers

from .models import Analyst

class AnalystSerializer(serializers.ModelSerializer):
    class Meta:
        model: Analyst
        fields = ["email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return Analyst.objects.create_user(**validated_data)