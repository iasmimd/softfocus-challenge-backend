from rest_framework import serializers

from .models import Registration

from geopy.geocoders import Nominatim
from geopy.distance import geodesic as GD

geolocator = Nominatim(user_agent="registrations")


class DateLocationError(Exception):
    ...


class RegistrationSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    class Meta:
        model = Registration
        fields = ["id", "farmer_name", "farmer_email", "latitude", "longitude", "address", "farmer_cpf", "tillage_type", "harvest_date", "cause", "last_modified", "analyst_id"]
        read_only_fields = ["analyst_id"]

    def get_address(self, obj):
        location = f"{obj.latitude}, {obj.longitude}"
        location_address = geolocator.reverse(location)

        return location_address.address


    def create(self, validated_data):
        registrations = Registration.objects.all()

        location_validated_data = f'{validated_data["latitude"]}, {validated_data["longitude"]}'

        for i in registrations:
            location_registration = f'{i.latitude}, {i.longitude}'
            if i.harvest_date == validated_data["harvest_date"] and GD(location_validated_data, location_registration).km <= 10:
                if i.cause != validated_data["cause"]:
                    raise DateLocationError("laalala")

        return Registration.objects.create(**validated_data)