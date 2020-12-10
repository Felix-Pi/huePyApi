from unittest import TestCase

from config import ip, api_key
from huePyApi.Hue import *
from huePyApi.enums.Alert import *
from huePyApi.enums.Bri import *
from huePyApi.enums.Ct import *

class TestGroup(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)

    def test_group_set_on(self):
        group = self.hue.get_group(1)
        group.set_on(True)

    def test_group_set_bri(self):
        group = self.hue.get_group(1)

        with self.assertRaises(Exception) as context:
            group.set_bri(int(Bri.MAX.value + 1))

        print(context.exception)
        self.assertTrue(isinstance(context.exception, ValueError))

        group.set_bri(Bri.MAX.value)

    def test_group_set_ct(self):
        group = self.hue.get_group(1)

        with self.assertRaises(Exception) as context:
            group.set_ct(int(Ct.MAX.value + 1))

        self.assertTrue(isinstance(context.exception, ValueError))

        group.set_ct(200)

    def test_group_set_alert(self):
        group = self.hue.get_group(1)
        group.set_alert(Alert.SELECT)

    def test_group_set_alert_wrong_parameter(self):
        group = self.hue.get_group(1)

        with self.assertRaises(Exception) as context:
            group.set_alert('select')

        self.assertTrue(isinstance(context.exception, TypeError))

    def test_group_set_scene(self):
        group = self.hue.get_group(1)
        scenes = self.hue.get_scenes_for_group(group)

        group.set_scene(scenes[1])
