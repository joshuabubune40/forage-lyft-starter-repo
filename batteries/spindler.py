from datetime import datetime
from battery import Battery

class SpindlerBattery(Battery):
    """
    Spindler battery implementation
    """

    def __init__(self, current_date=None, last_service_date=None):
        self.current_date = current_date if current_date else datetime.now()
        self.last_service_date = last_service_date if last_service_date else self.current_date

    def needs_service(self):
        self.current_date = datetime.today().date()
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3).date()
        if service_threshold_date < self.current_date:
            return True
        else:
            return False

