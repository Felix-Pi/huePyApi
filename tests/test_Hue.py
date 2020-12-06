from unittest import TestCase

from config import ip, api_key
from Hue import *


class TestHue(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)

    # groups
    def test_get_all_groups(self):
        groups = self.hue.getAllGroups()
        print(groups)

    def test_get_group(self):
        group = self.hue.getGroup(1)
        print(group)

    def test_group_set_on(self):
        group = self.hue.getGroup(1)
        group.setOn(True)

    def test_group_set_bri(self):
        group = self.hue.getGroup(1)
        group.setBri(355)

    def test_group_set_alert(self):
        group = self.hue.getGroup(1)
        group.setAlert('select')

    # lights
    def test_get_all_lights(self):
        lights = self.hue.getAllLights()
        print(lights)

    def test_get_light(self):
        light = self.hue.getLight(26)
        print(light)

    def test_light_set_on(self):
        light = self.hue.getLight(26)
        light.setOn(True)

    def test_light_set_bri(self):
        light = self.hue.getLight(26)
        light.setBri(255)

    def test_lights_set_alert(self):
        light = self.hue.getLight(26)
        light.setAlert('select')
