from battery.battery_type.splinder_battery import SplinderBattery
from battery.battery_type.nubbin_battery import NubbinBattery
from engine.engine_type.capulet_engine import CapuletEngine
from engine.engine_type.sternman_engine import StrenmanEngine
from engine.engine_type.willoughby_engine import WilloughbyEngine
from datetime import date
from car import Car

class CarFactory():
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        battery = SplinderBattery(current_date=current_date, last_service_date=last_service_date)
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        capulet = Car(engine=engine, battery=battery)
        return capulet
    
    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        battery = SplinderBattery(current_date=current_date, last_service_date=last_service_date)
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        glissade = Car(engine=engine, battery=battery)
        return glissade
    
    @staticmethod
    def create_palindrome(current_date : date, last_service_date : date, check_light_is_on : bool) -> Car:
        battery = SplinderBattery(current_date=current_date, last_service_date=last_service_date)
        engine = StrenmanEngine(check_light_is_on=check_light_is_on)
        palindrome = Car(engine, battery)
        return palindrome
    
    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        rorschach = Car(engine=engine, battery=battery)
        return rorschach
    
    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        battery = NubbinBattery(current_date=current_date, last_service_date=last_service_date)
        engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        thovex = Car(engine=engine, battery=battery)
        return thovex