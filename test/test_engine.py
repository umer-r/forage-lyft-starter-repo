import unittest
from engine.engine_type.capulet_engine import CapuletEngine
from engine.engine_type.sternman_engine import StrenmanEngine
from engine.engine_type.willoughby_engine import WilloughbyEngine

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30002
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        self.assertTrue(engine.needs_service())
        
    def test_engine_should_be_not_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        self.assertTrue(engine.needs_service())
        
    def test_engine_should_be_not_serviced(self):
        current_mileage = 60019
        last_service_mileage = 20
        engine = WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        self.assertFalse(engine.needs_service())
        
class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        check_light_is_on = True
        engine = StrenmanEngine(check_light_is_on=check_light_is_on)
        self.assertTrue(engine.needs_service())
        
    def test_engine_should_be_not_serviced(self):
        check_light_is_on = False
        engine = StrenmanEngine(check_light_is_on=check_light_is_on)
        self.assertFalse(engine.needs_service())
    