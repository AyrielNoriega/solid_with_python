

from typing import List

from lsp.symptom.trip import Trip


class Truck:
    def __init__(self, plate_number: str, odometer: float):
        self.plate_number: str = plate_number
        self.odometer: float = odometer
        self.trips: List[Trip] = []

    def add_trip(self, trip: Trip):
        self.trips.append(trip)
