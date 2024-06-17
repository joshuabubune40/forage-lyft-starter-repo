import unittest

from tires.carrigan import CarriganTire
from tires.octoprime import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        carrigan_tire = CarriganTire([0, 0.1, 1, 0.7, 0.4, 0.5])
        self.assertTrue(carrigan_tire.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        carrigan_tire = CarriganTire([0, 0.1, 0.3, 0.7, 0.4, 0.5])
        self.assertFalse(carrigan_tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        octoprime_tire = OctoprimeTire([0, 0.9, 1, 0.7, 0.4, 0.5])
        self.assertTrue(octoprime_tire.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        octoprime_tire = OctoprimeTire([0, 0.1, 0.3, 0.4, 0.6, 0.5])
        self.assertFalse(octoprime_tire.needs_service())