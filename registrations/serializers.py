from rest_framework import serializers
from traitlets import Type

from .models import Registration

from geopy.geocoders import Nominatim
from geopy.distance import geodesic as GD

geolocator = Nominatim(user_agent="registrations")


class DateLocationError(Exception):
    ...


class RegistrationSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    is_duplicate_registration = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = [
            "id",
            "farmer_name",
            "farmer_email",
            "latitude",
            "longitude",
            "address",
            "farmer_cpf",
            "tillage_type",
            "harvest_date",
            "cause",
            "is_duplicate_registration",
            "last_modified",
            "analyst_id",
        ]
        read_only_fields = ["analyst_id"]

    def get_address(self, obj):
        location = f"{obj.latitude}, {obj.longitude}"
        location_address = geolocator.reverse(location)

        self.location_validator_error(location_address)

        return location_address.address

    def get_is_duplicate_registration(self, obj):
        registrations = Registration.objects.all()

        location_validated_data = f"{obj.latitude}, {obj.longitude}"

        for i in registrations:
            location_registration = f"{i.latitude}, {i.longitude}"
            if (
                i.harvest_date == obj.harvest_date
                and GD(location_validated_data, location_registration).km <= 10
            ):
                if i.cause != obj.cause:
                    return True

                return False

    def location_validator_error(self, location):
        if not location:
            raise serializers.ValidationError(
                {"location": "Insira um valor válido para latitude e longitude"}
            )

    def create(self, validated_data):
        location = f'{validated_data["latitude"]}, {validated_data["longitude"]}'
        location_address = geolocator.reverse(location)

        self.location_validator_error(location_address)

        return Registration.objects.create(**validated_data)
