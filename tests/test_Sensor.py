from unittest import TestCase

from config import ip, api_key
from huePyApi.Hue import *


# ToDo: implement Sonsor tests
class TestSensor(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)

    def test_get_sensor_id(self):
        self.fail()

    def test_get_name(self):
        self.fail()

    def test_get_sensor_type(self):
        self.fail()

    def test_get_modelid(self):
        self.fail()

    def test_get_lastupdated(self):
        self.fail()


class TestPresenceSensor(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)

    def test_get_presence(self):
        self.fail()


class TestLightLevelSensor(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)

    def test_get_light_level(self):
        self.fail()

    def test_get_dark(self):
        self.fail()

    def test_get_daylight(self):
        self.fail()


class TestTemperatureSensor(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)

    def test_get_temperature(self):
        temperature_sensor = self.hue.get_sensor(86)
        temperature = temperature_sensor.get_temperature()
        print(temperature_sensor.get_temperature())
        print(temperature_sensor.get_temperature_in_celsius())
        print(temperature_sensor.get_temperature_formatted())
