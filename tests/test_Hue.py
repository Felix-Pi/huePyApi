from unittest import TestCase

from config import ip, api_key
from huePyApi.Hue import *


class TestHue(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)

    # requests

    # groups
    def test_get_all_groups(self):
        groups = self.hue.get_all_groups()
        print(groups)

    def test_get_group(self):
        group = self.hue.get_group(1)
        print(group)

    # lights
    def test_get_all_lights(self):
        lights = self.hue.get_all_lights()
        print(lights)

    def test_get_light(self):
        light = self.hue.get_light(26)
        print(light)

    # scenes
    def test_get_all_scenes(self):
        scenes = self.hue.get_all_scenes()
        print(scenes)

    def test_that_scene_id_length_always_is_15(self):
        scenes = self.hue.get_all_scenes()
        for scene in scenes:
            assert 15 == len(scene.scene_id)

    def test_get_scene(self):
        scene = self.hue.get_scene('7FQzspPLCTwjAsL')
        print(scene)

    def test_get_scenes_for_group(self):
        group = self.hue.get_group(1)
        scenes = self.hue.get_scenes_for_group(group)
        print(scenes)

    # resourcelinks
    def test_get_all_resourcelinks(self):
        resourcelinks = self.hue.get_all_resourcelinks()
        print(resourcelinks)

    def test_get_resourcelink(self):
        scene = self.hue.get_resourcelink(5287)
        print(scene)

    # sensors
    def test_get_all_sensors(self):
        sensors = self.hue.get_all_sensors()

        for sensor in sensors:
            print(sensor)

    def test_get_sensors_for_modelid(self):
        sensors = self.hue.get_sensors_for_modelid(SensorModel.HUE_HOMEAWAY)

        for sensor in sensors:
            print(sensor)
            # print(sensor.name, '-', sensor.modelid)

    def test_get_sensor(self):
        sensor = self.hue.get_sensor(64)
        print(sensor.config)
        print(sensor.get_battery())
        print(sensor)

    def test_test_extern_method(self):
        self.hue.test_extern_method()
