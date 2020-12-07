from unittest import TestCase
from Hue import *

class TestLight(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)

    def test_light_set_on(self):
        light = self.hue.getLight(26)
        light.setOn(True)

    def test_light_set_bri(self):
        light = self.hue.getLight(26)
        light.setBri(255)

    def test_lights_set_alert(self):
        light = self.hue.getLight(26)
        light.setAlert('select')
