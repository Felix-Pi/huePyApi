from unittest import TestCase

from config import ip, api_key
from huePyApi.Hue import *
from huePyApi.enums.Alert import *
from huePyApi.enums.Bri import *
from huePyApi.enums.Ct import *

class TestLight(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)

    def test_light_set_on(self):
        light = self.hue.get_light(5)
        light.set_on(True)

    def test_light_set_bri(self):
        light = self.hue.get_light(5)

        with self.assertRaises(Exception) as context:
            light.set_bri(Bri.MAX.value + 1)

        self.assertTrue(isinstance(context.exception, ValueError))

        light.set_bri(Bri.MAX.value)

    def test_light_set_ct(self):
        light = self.hue.get_light(5)

        light.set_ct(Ct.MAX.value)


    def test_lights_set_alert(self):
        light = self.hue.get_light(5)

        with self.assertRaises(Exception) as context:
            light.set_alert('select')

        self.assertTrue(isinstance(context.exception, TypeError))

    def test_lights_set_alert_wrong_parameter(self):
        light = self.hue.get_light(5)
        light.set_alert(Alert.SELECT)

