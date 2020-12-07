import json
from Alert import *


class Light:
    def __init__(self, hue, light_id, name, on, bri, ct, alert):
        self.hue = hue
        self.light_id = str(light_id)
        self.name = str(name)
        self.on = bool(on)

        self.bri = bri
        if bri is not None:
            self.bri = int(bri)

        self.ct = ct
        if ct is not None:
            self.ct = int(ct)

        self.alert = str(alert)

    def __repr__(self):
        return 'Light(id={}, on={}, bri={}, ct={}, alert={})'.format(self.light_id, self.on, self.bri,
                                                                     self.ct,
                                                                     self.alert)

    def getLights(self):
        raise NotImplementedError("Not implemented yet!")

    def setOn(self, state=True):
        state = json.dumps({"on": state})
        return self.hue.put(self.hue.lights_url + '/' + str(self.light_id) + '/state', state)

    def setBri(self, bri):
        if not 1 <= bri <= 254:
            raise ValueError('bri must be int between 1 and 254')

        state = json.dumps({"bri": bri})
        return self.hue.put(self.hue.lights_url + '/' + str(self.light_id) + '/state', state)

    def setAlert(self, alert):
        if not isinstance(alert, Alert):
            raise TypeError('alert must be an instance of Alert Enum')

        state = json.dumps({"alert": alert.value})
        return self.hue.put(self.hue.lights_url + '/' + str(self.light_id) + '/state', state)
