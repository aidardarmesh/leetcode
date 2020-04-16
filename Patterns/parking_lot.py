# Parking > Floor > Slot
# SlotSize?
# VehicleTypes?
# Several Parkings?
# Several Floors?

from enum import Enum


class ParkingStatus(Enum):
    EMPTY = 0
    FULL = 1


class VehicleTypes(Enum):
    BIKE = 0
    SEDAN = 1
    BUS = 2
    TRUCK = 3


class SlotSize(Enum):
    SMALL = (VehicleTypes.BIKE,)
    MEDIUM = (VehicleTypes.BIKE, VechileTypes.SEDAN,)
    LARGE = (VehicleTypes.BIKE, VechileTypes.SEDAN,
             VehicleTypes.BUS, VehicleTypes.TRUCK,)


class ParkingSlot:
    
    def __init__(self, id, size, status):
        self.id = id
        self.size = size
        self.status = status
    
    def park(self, vehicle):
        self.vehicle = vehicle
        self.status = ParkingStatus.FULL
    
    def empty(self):
        self.vehicle = None
        self.status = ParkingStatus.EMPTY


class Floor:

    def __init__(self, floor_id, floor_name, slots):
        self.floor_id = floor_id
        self.floor_name = floot_name
        self.slots = slots
    
    def empty(self):
        for slot in self.slots:
            slot.empty()


class Parking:

    def __init__(self, id, name, address, floors):
        self.id = id
        self.name = name
        self.address = address
        self.floors = floors
    
    def empty(self):
        for floor in self.floors:
            floor.empty()


from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


# Same for Seda, Bus, Truck
class Bike(Vehicle):

    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def get_type(self):
        return VehicleTypes.BIKE
    
    def get_info(self):
        return f"{self.brand}, {self.model}, {self.number}"


class ParkingDetails:

    def __init__(self, vehicle, start, end):
        self.vehicle = vehicle
        self.start = start
        self.end = end


from datetime import datetime


PRICING = {
    VehicleTypes.BIKE: 1,
    VehicleTypes.SEDAN: 2,
    VehicleTypes.BUS: 3,
    VehicleTypes.TRUCK: 4,
}


class FareController:
    
    def __init__(self):
        self.log = {}
    
    def on_vehicle_entry(self, vehicle, parking):
        self.log[vehicle] = ParkingDetails(vehicle, parking, datetime.now())
    
    def on_vehicle_exit(self, vehicle, parking):
        self.log[vehicle] = ParkingDetails(vehicle, parking, datetime.now())
    
    def get_fare(self, vehicle):
        self.details = self.log.get(vehicle)

        return PRICING[self.vehicle.get_type()] * (details.end - details.start)
