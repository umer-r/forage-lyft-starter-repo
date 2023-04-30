from battery.battery import Battery
from dateutil.relativedelta import relativedelta

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        next_service_date = self.last_service_date + relativedelta(years=3)
        return self.current_date > next_service_date