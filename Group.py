import json
from Alert import *


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

    def getLights(self):
        raise NotImplementedError("Not implemented yet!")

    def setOn(self, state=True):
        state = json.dumps({"on": state})
        return self.hue.put(self.hue.groups_url + '/' + str(self.group_id) + '/action', state)

    def setBri(self, bri):
        if not 1 <= bri <= 254:
            raise ValueError('bri must be int between 1 and 254')
        state = json.dumps({"bri": bri})
        return self.hue.put(self.hue.groups_url + '/' + str(self.group_id) + '/action', state)

    def setAlert(self, alert):
        if not isinstance(alert, Alert):
            raise TypeError('alert must be an instance of Alert Enum')

        state = json.dumps({"alert": alert.value})
        return self.hue.put(self.hue.groups_url + '/' + str(self.group_id) + '/action', state)

    def setScene(self, scene):
        state = json.dumps({"scene": scene.scene_id})
        return self.hue.put(self.hue.groups_url + '/' + str(self.group_id) + '/action', state)
