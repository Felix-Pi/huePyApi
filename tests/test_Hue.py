from unittest import TestCase

from config import ip, api_key
from huePyApi.Hue import *


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

    def test_get_scenes_for_group(self):
        group = self.hue.getGroup(1)
        scenes = self.hue.getScenesForGroup(group)
        print(scenes)

    # resourcelinks
    def test_get_all_resourcelinks(self):
        resourcelinks = self.hue.getAllResourcelinks()
        print(resourcelinks)

    def test_get_resourcelink(self):
        scene = self.hue.getResourcelink(5287)
        print(scene)

    # sensors
    def test_get_all_sensors(self):
        sensors = self.hue.getAllSensors()
        print(len(sensors), sensors)

        for sensor in sensors:
            print(sensor)
            # print(sensor.name, '-', sensor.modelid)

    def test_get_sensors_for_modelid(self):
        sensors = self.hue.getSensorsForModelid(Sensor_model.HUE_MOTION_SENSOR)

        for sensor in sensors:
            print(sensor)
            # print(sensor.name, '-', sensor.modelid)

    def test_get_sensor(self):
        sensor = self.hue.getSensor(86)
        print(sensor)
