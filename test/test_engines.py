import unittest
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        current_mg = 30011
        last_service_mg = 10
        capulet = CapuletEngine(current_mg, last_service_mg)

        self.assertTrue(capulet.needs_service())
    
    def test_engine_negative_mileage(self):
        current_mg = 10
        last_service_mg = 30011
        capulet = CapuletEngine(current_mg, last_service_mg)

        self.assertFalse(capulet.needs_service())
    
    def test_engine_does_not_need_service(self):
        current_mg = 200
        last_service_mg = 30200
        capulet = CapuletEngine(current_mg, last_service_mg)

        self.assertFalse(capulet.needs_service())
    
    def test_engine_negative_values(self):
        current_mg = -22993
        last_service_mg = 394993
        capulet = CapuletEngine(current_mg, last_service_mg)

        self.assertFalse(capulet.needs_service())

    def test_engine_string_mileage(self):
        capulet = CapuletEngine('-454', '-434')

        with self.assertRaises(TypeError):
            capulet.needs_service()

    def test_engine_list_mileage(self):
        capulet = CapuletEngine([-454], [-434])

        with self.assertRaises(TypeError):
            capulet.needs_service()

    def test_engine_dict_mileage(self):
        capulet = CapuletEngine({'another_year': 23}, {'last_year': 3444})

        with self.assertRaises(TypeError):
            capulet.needs_service()

    def test_engine_str_int_mileage(self):
        capulet = CapuletEngine('adcdc', -434)

        with self.assertRaises(TypeError):
            capulet.needs_service()


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        current_mg = 60011
        last_service_mg = 10
        capulet = WilloughbyEngine(current_mg, last_service_mg)

        self.assertTrue(capulet.needs_service())
    
    def test_engine_negative_mileage(self):
        current_mg = 10
        last_service_mg = 60011
        capulet = WilloughbyEngine(current_mg, last_service_mg)

        self.assertFalse(capulet.needs_service())
    
    def test_engine_does_not_need_service(self):
        current_mg = 200
        last_service_mg = 60200
        capulet = WilloughbyEngine(current_mg, last_service_mg)

        self.assertFalse(capulet.needs_service())
    
    def test_engine_negative_values(self):
        current_mg = 542993
        last_service_mg = -394993
        capulet = WilloughbyEngine(current_mg, last_service_mg)

        self.assertTrue(capulet.needs_service())

    def test_engine_string_mileage(self):
        capulet = WilloughbyEngine('-454', '-434')

        with self.assertRaises(TypeError):
            capulet.needs_service()

    def test_engine_list_mileage(self):
        capulet = WilloughbyEngine([-454], [-434])

        with self.assertRaises(TypeError):
            capulet.needs_service()

    def test_engine_dict_mileage(self):
        capulet = WilloughbyEngine({'another_year': 23}, {'last_year': 3444})

        with self.assertRaises(TypeError):
            capulet.needs_service()

    def test_engine_str_int_mileage(self):
        capulet = WilloughbyEngine('adcdc', -434)

        with self.assertRaises(TypeError):
            capulet.needs_service()


class TestStarnmanEngine(unittest.TestCase):
    def test_engine_needs_service(self):
        capulet = SternmanEngine(True)

        self.assertTrue(capulet.needs_service())
    
    def test_engine_does_not_need_service(self):
        capulet = SternmanEngine(False)

        self.assertFalse(capulet.needs_service())

    def test_engine_string_mileage(self):
        capulet = SternmanEngine('-4df')

        self.assertFalse(capulet.needs_service())

    def test_engine_list_mileage(self):
        capulet = SternmanEngine([-454])

        self.assertFalse(capulet.needs_service())

    def test_engine_dict_mileage(self):
        capulet = SternmanEngine({'another_year': 23})

        self.assertFalse(capulet.needs_service())

    def test_engine_str_int_mileage(self):
        capulet = SternmanEngine(-434)

        self.assertFalse(capulet.needs_service())
