from rest_framework import viewsets, filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Flight, Passenger
from .serializers import FlightSerializer, PassengerSerializer

# Pagination Class
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Flight ViewSet
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['flight_number', 'origin', 'destination']

# Passenger ViewSet
class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email']

    def create(self, request, *args, **kwargs):
        # Ensure the flight_id is passed and valid
        flight_id = request.data.get('flight_id')
        if not flight_id:
            return Response({"error": "Flight ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            flight = Flight.objects.get(id=flight_id)
        except Flight.DoesNotExist:
            return Response({"error": "Flight not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if the flight is fully booked
        if flight.passengers.count() >= flight.capacity:
            return Response({"error": "This flight is fully booked."}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)
