# Simplified Airline Booking System

## Overview

This project is a simplified API for an airline booking system built with Django and Django REST Framework. It provides CRUD operations for managing flights and passengers, including relationships and constraints to simulate a real-world booking system.

## Project Structure

- **Models**: Defines the data structure for Flights and Passengers.
- **Serializers**: Converts model instances to JSON and vice versa.
- **Views/ViewSets**: Handles the logic for CRUD operations and integrates with serializers.

## Requirements

- Python 3.12.5
- Django 3.2
- Django REST Framework

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/WayneNganju/API-ExtraCredit-Assignment-146832
cd API-ExtraCredit-Assignment-146832
```

### 2. Create a Virtual Environment

```bash
python -m venv myVenv
source myVenv/bin/activate  # On Windows use `myVenv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install Django==3.2
djangorestframework==3.14.0
mysqlclient==2.1.1


```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

### Flights

- **List Flights**: `GET /api/flights/`
- **Retrieve Flight**: `GET /api/flights/{id}/`
- **Create Flight**: `POST /api/flights/`
- **Update Flight**: `PUT /api/flights/{id}/`
- **Delete Flight**: `DELETE /api/flights/{id}/`

### Passengers

- **List Passengers**: `GET /api/passengers/`
- **Retrieve Passenger**: `GET /api/passengers/{id}/`
- **Create Passenger**: `POST /api/passengers/`
- **Update Passenger**: `PUT /api/passengers/{id}/`
- **Delete Passenger**: `DELETE /api/passengers/{id}/`

## Detailed Explanation

### Models

**Flight**

- `flight_number`: A unique identifier for each flight.
- `departure`: The date and time of flight departure.
- `arrival`: The date and time of flight arrival.
- `origin`: The departure airport.
- `destination`: The arrival airport.
- `capacity`: The total number of seats available on the flight.

**Passenger**

- `first_name`: The passenger's first name.
- `last_name`: The passenger's last name.
- `email`: The passenger's unique email address.
- `phone_number`: The passenger's contact number.
- `flight`: A foreign key linking the passenger to a specific flight using flight id. 

### Serializers

**FlightSerializer**

- Serializes all fields of the `Flight` model.

**PassengerSerializer**

- Serializes all fields of the `Passenger` model.
- Includes a nested `FlightSerializer` to provide details about the related flight.
- Validates that the flight is not fully booked before allowing the creation of a new passenger.

### Views/ViewSets

**FlightViewSet**

- **List Flights**: Returns a paginated list of all flights.
- **Retrieve Flight**: Provides details of a single flight by ID.
- **Create Flight**: Allows the creation of a new flight.
- **Update Flight**: Updates details of an existing flight.
- **Delete Flight**: Deletes a flight by ID.
- **Filtering**: Allows search by `flight_number`, `origin`, and `destination`.

**PassengerViewSet**

- **List Passengers**: Returns a paginated list of all passengers.
- **Retrieve Passenger**: Provides details of a single passenger by ID.
- **Create Passenger**: Allows the creation of a new passenger. Ensures the flight is not fully booked before creating a passenger.
- **Update Passenger**: Updates details of an existing passenger.
- **Delete Passenger**: Deletes a passenger by ID.
- **Filtering**: Allows search by `first_name`, `last_name`, and `email`.

### Design Decisions

- **Pagination**: Implemented with `StandardResultsSetPagination` to handle large datasets.
- **Filtering**: Added search filters to the viewsets to allow querying based on relevant fields.
- **Validation**: Ensured that passengers cannot be added to fully booked flights.

## Contact

For questions or further information, please contact wayne.nganju@strathmore.edu
