import json

from config import ip, api_key

import requests
import time


class Hue:
    def __init__(self, ip, api_key, notification=False):
        self.ip = ip
        self.api_key = api_key
        self.api_url = 'http://' + self.ip + '/api/' + self.api_key
        self.groups_url = 'groups'
        self.lights_url = 'lights'
        self.scenes_url = 'scenes'

    def validate_request(self, req):
        req_json = req.json()
        # print('validate_request', req.json())
        if isinstance(req_json, list):
            req_json = req_json[0]

        if 'error' in req_json:
            raise Exception(req_json['error'])

    def put(self, url_suffix, query):
        url = self.api_url + '/' + url_suffix
        print(url, query)
        req = requests.put(url, data=query)

        self.validate_request(req)
        return req.json()

    def get(self, url_suffix, query):
        url = self.api_url + '/' + url_suffix
        print(url, query)
        req = requests.get(url, query)

        self.validate_request(req)
        return req.json()

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

    def parseLight(self, light_id, light):
        print(light)
        name = light['name']
        on = light['state']['on']
        bri = light['state']['bri']
        ct = None
        if 'ct' in light['state']:
            ct = light['state']['ct']
        alert = light['state']['alert']

        return Light(self, light_id, name, on, bri, ct, alert)

    def getAllLights(self):
        lights = self.get(self.lights_url, '')
        return [self.parseLight(light_id, lights[light_id]) for light_id in lights]

    def getLight(self, group_id):
        raise NotImplementedError("Not implemented yet!")

    def getAllScenes(self):
        raise NotImplementedError("Not implemented yet!")

    def getScene(self, group_id):
        raise NotImplementedError("Not implemented yet!")


class Group:
    def __init__(self, hue, group_id, name, lights, on, bri, ct, alert):
        self.hue = hue
        self.group_id = group_id
        self.name = name
        self.lights = lights
        self.on = on
        self.bri = bri
        self.ct = ct
        self.alert = alert

    def __repr__(self):
        return 'Group(id={}, lights={}, on={}, bri={}, ct={}, alert={})'.format(self.group_id, self.lights, self.on,
                                                                                self.bri,
                                                                                self.ct,
                                                                                self.alert)

    def getLights(self):
        raise NotImplementedError("Not implemented yet!")

    def setOn(self, state=True):
        state = json.dumps({"on": state})
        self.hue.put(self.hue.groups_url + '/' + str(self.id) + '/action', state)

    def setBri(self, bri):
        state = json.dumps({"bri": bri})
        self.hue.put(self.hue.groups_url + '/' + str(self.id) + '/action', state)

    def setAlert(self, alert):
        state = json.dumps({"alert": alert})
        self.hue.put(self.hue.groups_url + '/' + str(self.id) + '/action', state)



class Light:
    def __init__(self, hue, light_id, name, on, bri, ct, alert):
        self.hue = hue
        self.light_id = light_id
        self.name = name
        self.on = on
        self.bri = bri
        self.ct = ct
        self.alert = alert

    def __repr__(self):
        return 'Light(id={}, on={}, bri={}, ct={}, alert={})'.format(self.light_id, self.on, self.bri,
                                                                                self.ct,
                                                                                self.alert)

    def getLights(self):
        raise NotImplementedError("Not implemented yet!")

    def setOn(self):
        raise NotImplementedError("Not implemented yet!")

    def setBri(self):
        raise NotImplementedError("Not implemented yet!")

    def setAlert(self):
        raise NotImplementedError("Not implemented yet!")


class Scene:
    def __init__(self, id, name, group, lights, lightstates):
        self.id = id
        self.name = name
        self.on = group
        self.bri = lights
        self.ct = lightstates
