from tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, wear_sensor_values):
        self.wear_sensor_values = wear_sensor_values
    
    def needs_service(self):
        return sum(self.wear_sensor_values) >= 3