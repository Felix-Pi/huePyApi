from unittest import TestCase
from Hue import *


class TestGroup(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)

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
