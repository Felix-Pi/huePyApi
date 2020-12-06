from unittest import TestCase

from Hue import *


class TestHue(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)

    def test_get_all_scenes(self):
        scenes = self.hue.getAllScenes()
        print(scenes)

    def test_get_scene_by_group_id(self):
        scenes = self.hue.getSceneByGroupId(1)
        print(scenes)
