from Parking.constants import SPACE_MAPPING, VehicleType, PRICE_PER_MINUTE


class Vehicle:

    def __init__(self, license_number, vehicle_type, ticket=None):
        self.__license_number = license_number
        self.__type = vehicle_type
        self.__ticket = ticket
        self.__space = SPACE_MAPPING[vehicle_type]

    def get_licence_number(self):
        return self.__license_number


class Car(Vehicle):
    def __init__(self, license_number, ticket=None):
        super().__init__(license_number, VehicleType.Car.value, ticket)


class Bike(Vehicle):
    def __init__(self, license_number, ticket=None):
        super().__init__(license_number, VehicleType.Bike.value, ticket)


class Bus(Vehicle):
    def __init__(self, license_number, ticket=None):
        super().__init__(license_number, VehicleType.Bus.value, ticket)


class Ticket:

    def __init__(self, ticket_id, timestamp, price=None):
        self.__id = ticket_id
        self.__timestamp = timestamp
        self.__price = price

    def set_ticket_price_by_time(self, minutes):
        price = minutes * PRICE_PER_MINUTE
        self.__price = price


class ParkingLot:

    def __init__(self, parking_id, level, is_empty, vehicle=None, price=None):
        self.__id = parking_id
        self.__level = level
        self.__is_empty = is_empty
        self.__price = price
        self.__vehicle = vehicle

    def set_ticket_price_by_time(self, minutes):
        price = minutes * PRICE_PER_MINUTE
        self.__price = price

    def assign_vehicle(self, vehicle):
        self.__vehicle = vehicle

    def remove_vehicle(self):
        self.__vehicle = None

    def get_is_empty(self):
        return self.__is_empty

    def get_parking_id(self):
        return self.__id

    def get_vehicle(self):
        return self.__vehicle

    def set_vehicle(self, vehicle):
        self.__vehicle = vehicle

    def set_is_empty(self, is_empty):
        self.__is_empty = is_empty
