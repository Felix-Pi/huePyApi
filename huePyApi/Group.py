import json
from huePyApi.enums.Alert import *
from huePyApi.enums.Bri import *
from huePyApi.enums.Ct import *


def parse_group(hue, group_id, group):
    name = group['name']
    lights = group['lights']
    on = group['action']['on']
    bri = group['action']['bri']
    ct = None
    if 'ct' in group['action']:
        ct = group['action']['ct']

    alert = group['action']['alert']

    return Group(hue, group_id, name, lights, on, bri, ct, alert)


class Group:
    def __init__(self, hue, group_id, name, lights, on, bri, ct, alert):
        self.hue = hue
        self.group_id = str(group_id)
        self.name = str(name)
        self.lights = lights
        self.on = bool(on)

        self.bri = bri
        if bri is not None:
            self.bri = int(bri)

        self.ct = ct
        if ct is not None:
            self.ct = int(ct)

        self.alert = str(alert)

    def __repr__(self):
        return 'Group(id={}, lights={}, on={}, bri={}, ct={}, alert={})'.format(self.group_id, self.lights, self.on,
                                                                                self.bri,
                                                                                self.ct,
                                                                                self.alert)

    def get_lights(self):
        raise NotImplementedError("Not implemented yet!")

    def set_on(self, state=True):
        state = json.dumps({"on": state})
        return self.hue.put(self.hue.groups_url + '/' + self.group_id + '/action', state)

    def set_bri(self, bri):
        if not Bri.MIN.value <= bri <= Bri.MAX.value:
            raise ValueError('bri must be int between ' + str(Bri.MIN.value) + ' and ' + str(Bri.MAX.value))
        state = json.dumps({"bri": bri})
        return self.hue.put(self.hue.groups_url + '/' + self.group_id + '/action', state)

    def set_ct(self, ct):
        if not Ct.MIN.value <= ct <= Ct.MAX.value:
            raise ValueError('ct must be int between ' + str(Ct.MIN.value) + ' and ' + str(Ct.MAX.value))

        state = json.dumps({"ct": ct})
        return self.hue.put(self.hue.groups_url + '/' + self.group_id + '/action', state)

    def set_alert(self, alert):
        if not isinstance(alert, Alert):
            raise TypeError('alert must be an instance of Alert Enum')

        state = json.dumps({"alert": alert.value})
        return self.hue.put(self.hue.groups_url + '/' + self.group_id + '/action', state)

    def set_scene(self, scene):
        self.set_scene_by_id(scene.scene_id)

    def set_scene_by_id(self, scene_id):
        state = json.dumps({"scene": scene_id})
        return self.hue.put(self.hue.groups_url + '/' + self.group_id + '/action', state)
