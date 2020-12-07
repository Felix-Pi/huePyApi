from unittest import TestCase

from config import ip, api_key
from Hue import *



class TestLight(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)

    def test_light_set_on(self):
        light = self.hue.getLight(26)
        light.setOn(True)

    def test_light_set_bri(self):
        light = self.hue.getLight(26)

        with self.assertRaises(Exception) as context:
            light.setBri(355)

        self.assertTrue(isinstance(context.exception, ValueError))

        light.setBri(254)

    def test_light_set_ct(self):
        lights = self.hue.getAllLights()
        print(lights)
        light = self.hue.getLight(26)



    def test_lights_set_alert(self):
        light = self.hue.getLight(26)

        with self.assertRaises(Exception) as context:
            light.setAlert('select')

        self.assertTrue(isinstance(context.exception, TypeError))

    def test_lights_set_alert_wrong_parameter(self):
        light = self.hue.getLight(26)
        light.setAlert(Alert.SELECT)

