from unittest import TestCase
from Hue import *


class TestResourcelink(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)

        self.dummy_links = ['/scenes/7FQzspPLCTwjAsL', '/rules/4', '/sensors/66', '/groups/1']
        self.dummy_resourcelink = Resourcelink(self.hue, 'dummy_id', 10013, 'dumy dimmer switch', 'Dimmer switch',
                                               self.dummy_links)

    def test_get_linked_scenes(self):
        scenes = self.dummy_resourcelink.getLinkedScenes()
        print(scenes)
        assert scenes[0] == '7FQzspPLCTwjAsL'

    def test_get_scenes_from_dimmer_switch(self):
        scenes = self.hue.getResourcelink(5287).getLinkedScenes()
        ['7FQzspPLCTwjAsL', 'im8gR8q5x', 'zGbHK7jJX0TpRkK', 'nya7J5WRbtT0XwP', 'U7xwqZM8lcV3fUU']
        print(scenes)

    def test_get_linked_rules(self):
        rules = self.dummy_resourcelink.getLinkedRules()
        print(rules)
        assert rules[0] == '4'

    def test_get_linked_sensors(self):
        sensors = self.dummy_resourcelink.getLinkedSensors()
        print(sensors)
        assert sensors[0] == '66'

    def test_get_linked_groups(self):
        groups = self.dummy_resourcelink.getLinkedGroups()
        print(groups)
        assert groups[0] == '1'
