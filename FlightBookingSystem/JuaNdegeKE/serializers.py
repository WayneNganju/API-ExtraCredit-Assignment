from rest_framework import serializers
from .models import Flight, Passenger

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):
    flight_id = serializers.PrimaryKeyRelatedField(queryset=Flight.objects.all(), source='flight', write_only=True)
    flight = FlightSerializer(read_only=True)

    class Meta:
        model = Passenger
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'flight_id', 'flight']

    def validate(self, data):
        flight = data.get('flight')
        if flight.passengers.count() >= flight.capacity:
            raise serializers.ValidationError("This flight is fully booked.")
        return data
