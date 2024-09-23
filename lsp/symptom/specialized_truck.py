
from isp.symptom.trip import Trip
from isp.symptom.truck import Truck


class SpecializedTruck(Truck):
    def __init__(self, plate_number: str, odometer: float):
        super().__init__(plate_number, odometer)

    def add_trip(self, new_trip: Trip):
        super().add_trip(new_trip)

        for trip in self.trips:
            self.odometer += trip.distance
