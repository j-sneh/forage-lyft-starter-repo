from car import Car

from engine.model.capulet_engine import CapuletEngine
from engine.model.willoughby_engine import WilloughbyEngine
from engine.model.sternman_engine import SternmanEngine

from battery.model.nubbin_battery import NubbinBattery
from battery.model.spindler_battery import SpindlerBattery
from tires.model.carrigan_tires import CarriganTires
from tires.model.octoprime_tires import OctoprimeTires

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, sensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires(sensors)
        return Car(engine, battery, tires)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, sensors):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(sensors)
        return Car(engine, battery, tires)

    def create_palindrome(self, current_date, last_service_date, warning_light_on, sensors):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires(sensors)
        return Car(engine, battery, tires)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, sensors):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(sensors)
        return Car(engine, battery)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, sensors):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(sensors)
        return Car(engine, battery, tires)