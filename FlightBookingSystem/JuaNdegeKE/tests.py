from django.test import TestCase
from .models import Flight, Passenger

class FlightModelTests(TestCase):
    def setUp(self):
        self.flight = Flight.objects.create(
            flight_number="KQ123",
            departure="2024-09-01T10:00:00Z",
            arrival="2024-09-01T12:00:00Z",
            origin="NBO",  # Nairobi (Jomo Kenyatta International Airport)
            destination="MBA",  # Mombasa (Moi International Airport)
            capacity=150
        )

    def test_flight_str(self):
        self.assertEqual(str(self.flight), "KQ123 (NBO to MBA)")

class PassengerModelTests(TestCase):
    def setUp(self):
        self.flight = Flight.objects.create(
            flight_number="KQ123",
            departure="2024-09-01T10:00:00Z",
            arrival="2024-09-01T12:00:00Z",
            origin="NBO",
            destination="MBA",
            capacity=150
        )
        self.passenger = Passenger.objects.create(
            first_name="Mary",
            last_name="Wanjiru",
            email="mary.wanjiru@example.com",
            phone_number="0712345678",
            flight=self.flight
        )

    def test_passenger_str(self):
        self.assertEqual(str(self.passenger), "Mary Wanjiru")

