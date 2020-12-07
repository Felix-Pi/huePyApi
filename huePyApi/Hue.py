from huePyApi.Group import Group
from huePyApi.Light import Light
from huePyApi.Scene import Scene
from huePyApi.Resourcelink import Resourcelink

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
        #print('put:', url, query)
        req = requests.put(url, data=query)

        self.validate_request(req)
        return req.json()

    def get(self, url_suffix, query):
        url = self.api_url + '/' + url_suffix
        #print('get: ', url, query)
        req = requests.get(url, query)

        self.validate_request(req)
        return req.json()

    # groups
    def getAllGroups(self):
        groups = self.get(self.groups_url, '')
        return [self.parseGroup(group_id, groups[group_id]) for group_id in groups]

    def getGroup(self, group_id):
        group = self.get(self.groups_url + '/' + str(group_id), '')
        return self.parseGroup(group_id, group)

    def parseGroup(self, group_id, group):
        name = group['name']
        lights = group['lights']
        on = group['action']['on']
        bri = group['action']['bri']
        ct = None
        if 'ct' in group['action']:
            ct = group['action']['ct']

        alert = group['action']['alert']

        return Group(self, group_id, name, lights, on, bri, ct, alert)

    # lights
    def parseLight(self, light_id, light):
       #print('parseLight:', light)
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

    def getAllLights(self):
        lights = self.get(self.lights_url, '')
        return [self.parseLight(light_id, lights[light_id]) for light_id in lights]

    def getLight(self, light_id):
        light = self.get(self.lights_url + '/' + str(light_id), '')
        return self.parseLight(light_id, light)

    # scenes
    def parseScene(self, scene_id, scene):
        #print('parseScene:', scene)
        name = scene['name']

        group = None
        if 'group' in scene:
            group = scene['group']

        lights = scene['lights']
        lightstates = None
        if 'lightstates' in scene:
            lightstates = scene['lightstates']

        return Scene(self, scene_id, name, group, lights, lightstates)

    def getAllScenes(self):
        scenes = self.get(self.scenes_url, '')
        return [self.parseScene(scene_id, scenes[scene_id]) for scene_id in scenes]

    def getScene(self, scene_id):
        scene = self.get(self.scenes_url + '/' + str(scene_id), '')
        return self.parseScene(scene_id, scene)

    def getScenesForGroup(self, group):
        scenes = self.getAllScenes()

        return [scene for scene in scenes if scene.group is not None and scene.group == group.group_id]

    # resourcelinks
    def parseResourcelink(self, rl_id, resourcelink):
        #print('parseResourcelink:', resourcelink)
        classid = resourcelink['classid']
        description = resourcelink['description']
        name = resourcelink['name']

        links = None
        if 'links' in resourcelink:
            links = resourcelink['links']

        return Resourcelink(self, rl_id, classid, description, name, links)

    def getAllResourcelinks(self):
        resourcelinks = self.get(self.resourcelink_url, '')
        return [self.parseResourcelink(rl_id, resourcelinks[rl_id]) for rl_id in resourcelinks]

    def getResourcelink(self, rl_id):
        resourcelink = self.get(self.resourcelink_url + '/' + str(rl_id), '')
        return self.parseResourcelink(rl_id, resourcelink)
