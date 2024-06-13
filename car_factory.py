from car import Car
from datetime import datetime

from engines.willoughby_engine import WilloughbyEngine
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine

from batteries.spindler import SpindlerBattery
from batteries.nubbin import NubbinBattery


class CarFactory:
    """
    Car factory implementation
    """

    def __init__(self):
        self._calliopes = []
        self._glissades = []
        self._palindromes = []
        self._rorschachs = []
        self._thovexs = []
    
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        from engines.model.calliope import Calliope

        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        calliope_car = Calliope(capulet_engine, spindler_battery)
        self._calliopes.append(calliope_car)

        return calliope_car
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        from engines.model.glissade import Glissade

        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        glissade_car = Glissade(willoughby_engine, spindler_battery)
        self._glissades.append(glissade_car)

        return glissade_car
    
    def create_palindrome(self, current_date, last_service_date, warning_light_on) -> Car:
        from engines.model.palindrome import Palindrome

        spindler_battery = SpindlerBattery(last_service_date, current_date)
        sternman_engine = SternmanEngine(warning_light_on)
        palindrome_car = Palindrome(sternman_engine, spindler_battery)
        self._palindromes.append(palindrome_car)

        return palindrome_car
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        from engines.model.rorschach import Rorschach

        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        rorschach_car = Rorschach(willoughby_engine, nubbin_battery)
        self._rorschachs.append(rorschach_car)

        return rorschach_car
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        from engines.model.thovex import Thovex

        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        thovex_car = Thovex(capulet_engine, nubbin_battery)
        self._thovexs.append(thovex_car)

        return thovex_car

