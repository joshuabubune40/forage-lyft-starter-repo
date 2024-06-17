from datetime import datetime

from car import Car


class Palindrome(Car):
    def __init__(self, engine, battery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else:
            return False
