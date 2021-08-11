from Parking.models import ParkingLot, Car, Bus, Bike, Ticket
from Parking.constants import VehicleType
import datetime

ParkingLot_one = ParkingLot(101, 1, True)
ParkingLot_two = ParkingLot(102, 1, True)
ParkingLot_three = ParkingLot(103, 1, True)
ParkingLot_four = ParkingLot(201, 2, True)
ParkingLot_five = ParkingLot(202, 2, True)
ParkingLot_six = ParkingLot(203, 2, True)
ParkingLot_seven = ParkingLot(301, 3, True)


Total_available_plots = [
    ParkingLot_one, ParkingLot_two, ParkingLot_three,
    ParkingLot_four, ParkingLot_five, ParkingLot_six, ParkingLot_seven
]


def park_vehicle(license_number, vehicle_type, ticket):
    vehicle = None
    if vehicle_type == VehicleType.Car.value:
        vehicle = Car(license_number, ticket)
    elif vehicle_type == VehicleType.Bus.value:
        vehicle = Bus(license_number, ticket)
    elif vehicle_type == VehicleType.Bike.value:
        vehicle = Bike(license_number, ticket)
    find_spot = find_available_parking_slot(vehicle_type)
    if not find_spot:
        return "No space left!"
    find_spot.set_is_empty(False)

    find_spot.set_vehicle(vehicle)
    return find_spot


def find_available_parking_slot(vehicle_type):
    for spot in Total_available_plots:
        if spot.get_is_empty():
            return spot
    return None


def check_vehicle_spot(parking_id, license_number):
    for spot in Total_available_plots:
        if spot.get_parking_id() == parking_id:
            vehicle = spot.get_vehicle()
            if vehicle is None:
                return None
            if vehicle.get_licence_number() == license_number:
                return spot
    return None


def run():
    ticket = Ticket("1", datetime.datetime.now())
    ans = park_vehicle("1234", VehicleType.Car.value, ticket)
    check_vehicle_spot(101, "1234")
    check_vehicle_spot(202, "1234")


if __name__ == '__main__':
    run()
