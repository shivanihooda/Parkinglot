from enum import Enum


class VehicleType(Enum):
    Bike = "Light"
    Car = "Compact"
    Bus = "Heavy"


SPACE_MAPPING = {
    VehicleType.Bike.value: 1,
    VehicleType.Car.value: 1,
    VehicleType.Bus.value: 3,
}

VEHICLE_MAPPING = {
    VehicleType.Bike: "Light",
    VehicleType.Car: 1,
    VehicleType.Bus: 3,
}

PRICE_PER_MINUTE = 1

PARKING_LOT_SPACE = {
    "1": {
        "1": False,
        "2": False
    }
}
