from tire import Tire


class CarriganTire(Tire):
    def __init__(self, wear_sensor_values):
        self.wear_sensor_values = wear_sensor_values
    
    def needs_service(self):
        wear_count = 0
        for n in self.wear_sensor_values:
            if n >= 0.9:
                wear_count += 1
        return wear_count >= 1