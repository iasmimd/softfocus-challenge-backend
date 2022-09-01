from rest_framework import serializers

from .models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ["id", "farmer_name", "farmer_email", "farmer_cpf", "tillage_type", "harvest_date", "cause", "last_modified", "analyst"]
        read_only_fields = ["analysts"]

    def create(self, validated_data):
        return Registration.objects.create(**validated_data)