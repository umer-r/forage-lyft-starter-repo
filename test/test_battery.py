from battery.battery_type.nubbin_battery import NubbinBattery
from battery.battery_type.splinder_battery import SpindlerBattery
import unittest
from datetime import datetime

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime(2024, 1, 1)
        last_service_date = datetime(2017, 1, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime(2024, 1, 1)
        last_service_date = datetime(2030, 1, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime(2024, 1, 1)
        last_service_date = datetime(2019, 1, 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime(2022, 1, 1)
        last_service_date = datetime(2021, 1, 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
