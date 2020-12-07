from unittest import TestCase

from config import ip, api_key
from Hue import *


class TestGroup(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)

    def test_group_set_on(self):
        group = self.hue.getGroup(1)
        group.setOn(True)

    def test_group_set_bri(self):
        group = self.hue.getGroup(1)

        with self.assertRaises(Exception) as context:
            group.setBri(355)

        self.assertTrue(isinstance(context.exception, ValueError))

        group.setBri(254)

    def test_group_set_alert(self):
        group = self.hue.getGroup(1)
        group.setAlert(Alert.SELECT)

    def test_group_set_alert_wrong_parameter(self):
        group = self.hue.getGroup(1)

        with self.assertRaises(Exception) as context:
            group.setAlert('select')

        self.assertTrue(isinstance(context.exception, TypeError))

    def test_group_set_scene(self):
        group = self.hue.getGroup(1)
        scenes = self.hue.getScenesForGroup(group)

        group.setScene(scenes[1])
