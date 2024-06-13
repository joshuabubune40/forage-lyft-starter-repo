from car import Car


class Rorschach(Car):
    def __init__(self, engine, battery):
        self._engine = engine
        self._battery = battery

    def needs_service(self):
        if self._engine.needs_service() or self._battery.needs_service():
            return True
        else:
            return False
