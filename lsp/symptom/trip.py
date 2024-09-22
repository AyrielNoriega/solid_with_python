
class Trip:
    def __init__(
        self,
        original_latitude: int,
        original_longitude: int,
        destination_latitude: int,
        destination_longitude: int,
        distance: float
    ):
        self.original_latitude = original_latitude
        self.original_longitude = original_longitude
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude
        self.distance = distance