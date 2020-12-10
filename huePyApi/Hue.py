from huePyApi.Group import Group
from huePyApi.Light import Light
from huePyApi.Scene import Scene
from huePyApi.Sensor import *
from huePyApi.Resourcelink import Resourcelink

from huePyApi.enums.SensorModel import SensorModel
from huePyApi.enums.SensorType import SensorType

import requests


class Hue:
    def __init__(self, ip, api_key):
        self.ip = ip
        self.api_key = api_key
        self.api_url = 'http://' + self.ip + '/api/' + self.api_key
        self.groups_url = 'groups'
        self.lights_url = 'lights'
        self.scenes_url = 'scenes'
        self.resourcelink_url = 'resourcelinks'
        self.sensors_url = 'sensors'

    # requests
    def validate_request(self, req):
        req_json = req.json()
        # print('validate_request', req.json())
        if isinstance(req_json, list):
            req_json = req_json[0]

        if 'error' in req_json:
            raise Exception(req_json['error'])

    def put(self, url_suffix, query):
        url = self.api_url + '/' + url_suffix
        # print('put:', url, query)
        req = requests.put(url, data=query)

        self.validate_request(req)
        return req.json()

    def get(self, url_suffix):
        url = self.api_url + '/' + url_suffix
        # print('get: ', url, query)
        req = requests.get(url)

        self.validate_request(req)
        return req.json()

    # groups
    def parse_group(self, group_id, group):
        name = group['name']
        lights = group['lights']
        on = group['action']['on']
        bri = group['action']['bri']
        ct = None
        if 'ct' in group['action']:
            ct = group['action']['ct']

        alert = group['action']['alert']

        return Group(self, group_id, name, lights, on, bri, ct, alert)

    def get_all_groups(self):
        groups = self.get(self.groups_url)
        return [self.parse_group(group_id, groups[group_id]) for group_id in groups]

    def get_group(self, group_id):
        group = self.get(self.groups_url + '/' + str(group_id))
        return self.parse_group(group_id, group)

    # lights
    def parse_light(self, light_id, light):
        # print('parseLight:', light)
        name = light['name']
        on = light['state']['on']
        bri = None
        if 'bri' in light['state']:
            bri = light['state']['bri']
        ct = None
        if 'ct' in light['state']:
            ct = light['state']['ct']
        alert = light['state']['alert']

        return Light(self, light_id, name, on, bri, ct, alert)

    def get_all_lights(self):
        lights = self.get(self.lights_url)
        return [self.parse_light(light_id, lights[light_id]) for light_id in lights]

    def get_light(self, light_id):
        light = self.get(self.lights_url + '/' + str(light_id))
        return self.parse_light(light_id, light)

    # scenes
    def parse_scene(self, scene_id, scene):
        # print('parseScene:', scene)
        name = scene['name']

        group = None
        if 'group' in scene:
            group = scene['group']

        lights = scene['lights']
        lightstates = None
        if 'lightstates' in scene:
            lightstates = scene['lightstates']

        return Scene(self, scene_id, name, group, lights, lightstates)

    def get_all_scenes(self):
        scenes = self.get(self.scenes_url)
        return [self.parse_scene(scene_id, scenes[scene_id]) for scene_id in scenes]

    def get_scene(self, scene_id):
        scene = self.get(self.scenes_url + '/' + str(scene_id))
        return self.parse_scene(scene_id, scene)

    def get_scenes_for_group(self, group):
        scenes = self.get_all_scenes()

        return [scene for scene in scenes if scene.group is not None and scene.group == group.group_id]

    # resourcelinks
    def parse_resourcelink(self, rl_id, resourcelink):
        # print('parseResourcelink:', resourcelink)
        classid = resourcelink['classid']
        description = resourcelink['description']
        name = resourcelink['name']

        links = None
        if 'links' in resourcelink:
            links = resourcelink['links']

        return Resourcelink(self, rl_id, classid, description, name, links)

    def get_all_resourcelinks(self):
        resourcelinks = self.get(self.resourcelink_url)
        return [self.parse_resourcelink(rl_id, resourcelinks[rl_id]) for rl_id in resourcelinks]

    def get_resourcelink(self, rl_id):
        resourcelink = self.get(self.resourcelink_url + '/' + str(rl_id))
        return self.parse_resourcelink(rl_id, resourcelink)

    # sensors
    def parse_sensor(self, sensor_id, sensor):
        # print('parseSensor:', sensor)
        name = sensor['name']
        sensor_type = sensor['type']
        modelid = sensor['modelid']
        lastupdated = sensor['state']['lastupdated']
        config = sensor['config']

        # HUE_MOTION_SENSOR
        if modelid == SensorModel.HUE_MOTION_SENSOR.value:

            if sensor_type == SensorType.HUE_MOTION_SENSOR_LIGHT_LEVEL.value:
                lightlevel = sensor['state']['lightlevel']
                dark = sensor['state']['dark']
                daylight = sensor['state']['daylight']
                return LightLevelSensor(self, sensor_id, name, sensor_type, modelid, lastupdated, config, lightlevel,
                                        dark,
                                        daylight)

            if sensor_type == SensorType.HUE_MOTION_SENSOR_PRESENCE.value:
                presence = sensor['state']['presence']
                return PresenceSensor(self, sensor_id, name, sensor_type, modelid, lastupdated, config, presence)

            if sensor_type == SensorType.HUE_MOTION_SENSOR_TEMPERATURE.value:
                temperature = sensor['state']['temperature']
                return TemperatureSensor(self, sensor_id, name, sensor_type, modelid, lastupdated, config, temperature)

        # HUE_DIMMER_SWITCH
        if modelid == SensorModel.HUE_DIMMER_SWITCH.value:
            return DimmerSwitch(self, sensor_id, name, sensor_type, modelid, lastupdated, config)

        # HUE_GEOFENCE
        if modelid == SensorModel.HUE_GEOFENCE.value:
            presence = sensor['state']['presence']
            return Geofence(self, sensor_id, name, sensor_type, modelid, lastupdated, config, presence)

        # HUE_GEOFENCE
        if modelid == SensorModel.HUE_DAYLIGHT_SENSOR.value:
            daylight = sensor['state']['daylight']
            return DaylightSensor(self, sensor_id, name, sensor_type, modelid, lastupdated, config, daylight)

        return Sensor(self, sensor_id, name, sensor_type, modelid, lastupdated, config)

    def get_all_sensors(self):
        sensors = self.get(self.sensors_url)
        return [self.parse_sensor(sensor_id, sensors[sensor_id]) for sensor_id in sensors]

    def get_sensors_for_modelid(self, modelid):
        if not isinstance(modelid, SensorModel):
            raise TypeError('modelid must be an instance of Sensor_model Enum')

        sensors = self.get_all_sensors()

        return [sensor for sensor in sensors if sensor.modelid is not None and sensor.modelid == modelid.value]

    def get_sensor(self, sensor_id):
        sensor = self.get(self.sensors_url + '/' + str(sensor_id))
        return self.parse_sensor(sensor_id, sensor)
