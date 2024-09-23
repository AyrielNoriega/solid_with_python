
from isp.symptom.trip import Trip
from isp.symptom.truck import Truck


class Program:
    INITIAL_DISTANCE = 10000

    def __init__(self):
        truck: Truck = Truck("ABC123", self.INITIAL_DISTANCE)

        truck.add_trip(
            Trip(
                original_latitude=0,
                original_longitude=0,
                destination_latitude=0,
                destination_longitude=0,
                distance=60.0
            )
        )

        if truck.odometer == self.INITIAL_DISTANCE:
            print("Odometer is correct")
        else:
            print("Odometer has been modified")


if __name__ == "__main__":
    Program()
    input("Press any key to continue...")
