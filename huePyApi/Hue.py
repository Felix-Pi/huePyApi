from huePyApi.Group import *
from huePyApi.Light import *
from huePyApi.Scene import *
from huePyApi.Sensor import *
from huePyApi.Resourcelink import *

import requests


class Hue:
    def __init__(self, ip, api_key):
        self.ip = ip
        self.test_bridge_connection()

        self.api_key = api_key
        self.api_url = 'http://' + self.ip + '/api/' + self.api_key

        self.groups_url = 'groups'
        self.lights_url = 'lights'
        self.scenes_url = 'scenes'
        self.resourcelink_url = 'resourcelinks'
        self.sensors_url = 'sensors'

    def test_bridge_connection(self):
        try:
            req = requests.get("http://" + self.ip, timeout=2)
            print(req)
        except Exception:
            print("Could not connect to bridge with ip " + self.ip)
            self.auto_discover_ip()

    def auto_discover_ip(self):
        discovery_url = 'https://discovery.meethue.com'
        print("Try to find bridge ip via " + discovery_url)
        req = requests.get(discovery_url)
        req_json = req.json()

        try:
            self.ip = req_json[0]['internalipaddress']
            print("Discovered bridge ip address: " + self.ip)
        except Exception:
            raise Exception("Connection error!")

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
    def get_all_groups(self):
        groups = self.get(self.groups_url)
        return [parse_group(self, group_id, groups[group_id]) for group_id in groups]

    def get_group(self, group_id):
        group = self.get(self.groups_url + '/' + str(group_id))
        return parse_group(self, group_id, group)

    # lights
    def get_all_lights(self):
        lights = self.get(self.lights_url)
        return [parse_light(self, light_id, lights[light_id]) for light_id in lights]

    def get_light(self, light_id):
        light = self.get(self.lights_url + '/' + str(light_id))
        return parse_light(self, light_id, light)

    # scenes
    def get_all_scenes(self):
        scenes = self.get(self.scenes_url)
        return [parse_scene(self, scene_id, scenes[scene_id]) for scene_id in scenes]

    def get_scene(self, scene_id):
        scene = self.get(self.scenes_url + '/' + str(scene_id))
        return parse_scene(self, scene_id, scene)

    def get_scenes_for_group(self, group):
        scenes = self.get_all_scenes()

        return [scene for scene in scenes if scene.group is not None and scene.group == group.group_id]

    # resourcelinks
    def get_all_resourcelinks(self):
        resourcelinks = self.get(self.resourcelink_url)
        return [parse_resourcelink(self, rl_id, resourcelinks[rl_id]) for rl_id in resourcelinks]

    def get_resourcelink(self, rl_id):
        resourcelink = self.get(self.resourcelink_url + '/' + str(rl_id))
        return parse_resourcelink(self, rl_id, resourcelink)

    # sensors
    def get_all_sensors(self):
        sensors = self.get(self.sensors_url)
        return [parse_sensor(self, sensor_id, sensors[sensor_id]) for sensor_id in sensors]

    def get_sensor(self, sensor_id):
        sensor = self.get(self.sensors_url + '/' + str(sensor_id))
        return parse_sensor(self, sensor_id, sensor)

    def get_sensors_for_modelid(self, modelid):
        if not isinstance(modelid, SensorModel):
            raise TypeError('modelid must be an instance of Sensor_model Enum')

        sensors = self.get_all_sensors()

        return [sensor for sensor in sensors if sensor.modelid is not None and sensor.modelid == modelid.value]
