from datetime import datetime
from battery import Battery

class SpindlerBattery(Battery):
    """
    Spindler battery implementation
    """

    def __init__(self, last_service_date=None, current_date=None):
        self.__current_date = current_date if current_date else datetime.now()
        self.__last_service_date = last_service_date if last_service_date else self.__current_date

    def needs_service(self):
        service_threshold_date = self.__last_service_date.replace(year=self.__last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False

