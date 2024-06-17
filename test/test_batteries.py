import unittest
from datetime import datetime

from batteries.nubbin import NubbinBattery
from batteries.spindler import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def test_battery_needs_service(self):
        today = datetime.now()
        last_five_years = today.replace(year=today.year - 5)
        nubbin = NubbinBattery(today, last_five_years)

        self.assertEqual(nubbin.needs_service(), True)

    def test_battery_date_today(self):
        today = datetime.now()
        same_year = today
        nubbin = NubbinBattery(today, same_year)

        self.assertFalse(nubbin.needs_service())

    def test_battery_date_none(self):
        nubbin = NubbinBattery()

        self.assertFalse(nubbin.needs_service())
    
    def test_battery_does_not_need_service(self):
        today = datetime.now()
        last_four_years = today.replace(year=today.year - 4)
        nubbin = NubbinBattery(today, last_four_years)

        self.assertFalse(nubbin.needs_service())


    def test_battery_integer_dates(self):
        nubbin = NubbinBattery(-454, -434)

        with self.assertRaises(AttributeError):
            nubbin.needs_service()

    def test_battery_string_dates(self):
        nubbin = NubbinBattery('-454', '-434')

        with self.assertRaises(AttributeError):
            nubbin.needs_service()

    def test_battery_list_dates(self):
        nubbin = NubbinBattery([-454], [-434])

        with self.assertRaises(AttributeError):
            nubbin.needs_service()

    def test_battery_dict_dates(self):
        nubbin = NubbinBattery({'another_year': datetime.now()}, {'last_year': datetime.now()})

        with self.assertRaises(AttributeError):
            nubbin.needs_service()

    def test_battery_str_int_dates(self):
        nubbin = NubbinBattery('adcdc', -434)

        with self.assertRaises(AttributeError):
            nubbin.needs_service()




class TestSpindlerBattery(unittest.TestCase):
    def test_battery_needs_service(self):
        today = datetime.now()
        last_five_years = today.replace(year=today.year - 5)
        nubbin = SpindlerBattery(today, last_five_years)

        self.assertTrue(nubbin.needs_service())

    def test_battery_date_today(self):
        today = datetime.now()
        same_year = today
        nubbin = SpindlerBattery(today, same_year)

        self.assertFalse(nubbin.needs_service())

    def test_battery_date_none(self):
        nubbin = SpindlerBattery()

        self.assertFalse(nubbin.needs_service())

    def test_battery_does_not_need_service(self):
        today = datetime.now()
        last_year = today.replace(year=today.year - 1)
        nubbin = SpindlerBattery(today, last_year)

        self.assertFalse(nubbin.needs_service())
    

    def test_battery_integer_dates(self):
        nubbin = SpindlerBattery(-454, -434)

        with self.assertRaises(AttributeError):
            nubbin.needs_service()

    def test_battery_string_dates(self):
        nubbin = SpindlerBattery('-454', '-434')

        with self.assertRaises(AttributeError):
            nubbin.needs_service()

    def test_battery_list_dates(self):
        nubbin = SpindlerBattery([-454], [-434])

        with self.assertRaises(AttributeError):
            nubbin.needs_service()

    def test_battery_dict_dates(self):
        nubbin = SpindlerBattery({'another_year': datetime.now()}, {'last_year': datetime.now()})

        with self.assertRaises(AttributeError):
            nubbin.needs_service()

    def test_battery_str_int_dates(self):
        nubbin = SpindlerBattery('adcdc', -434)

        with self.assertRaises(AttributeError):
            nubbin.needs_service()
