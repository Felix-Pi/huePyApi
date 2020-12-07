from unittest import TestCase

from Hue import *


class TestHue(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)

    # requests
    # groups
    def test_get_all_groups(self):
        groups = self.hue.getAllGroups()
        print(groups)

    def test_get_group(self):
        group = self.hue.getGroup(1)
        print(group)

    # lights
    def test_get_all_lights(self):
        lights = self.hue.getAllLights()
        print(lights)

    def test_get_light(self):
        light = self.hue.getLight(26)
        print(light)

    # scenes
    def test_get_all_scenes(self):
        scenes = self.hue.getAllScenes()
        print(scenes)

    def test_that_scene_id_length_always_is_15(self):
        scenes = self.hue.getAllScenes()
        for scene in scenes:
            assert 15 == len(scene.scene_id)

    def test_get_scene(self):
        scene = self.hue.getScene('7FQzspPLCTwjAsL')
        print(scene)

    def test_get_scenes_for_group_id(self):
        scenes = self.hue.getScenesForGroupId(1)
        print(scenes)

    # resourcelinks
    def test_get_all_resourcelinks(self):
        resourcelinks = self.hue.getAllResourcelinks()
        print(resourcelinks)

    def test_get_resourcelink(self):
        scene = self.hue.getResourcelink(5287)
        print(scene)
