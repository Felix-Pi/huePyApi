import json
from huePyApi.enums import *
from huePyApi.enums.Alert import *
from huePyApi.enums.Bri import *
from huePyApi.enums.Ct import *


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
        return 'Light(id={}, name={}, on={}, bri={}, ct={}, alert={})'.format(self.light_id, self.name, self.on,
                                                                              self.bri,
                                                                              self.ct,
                                                                              self.alert)

    def getLights(self):
        raise NotImplementedError("Not implemented yet!")

    def setOn(self, state=True):
        state = json.dumps({"on": state})
        return self.hue.put(self.hue.lights_url + '/' + self.light_id + '/state', state)

    def setBri(self, bri):
        if not Bri.MIN.value <= bri <= Bri.MAX.value:
            raise ValueError('bri must be int between ' + str(Bri.MIN.value) + ' and ' + str(Bri.MAX.value))

        state = json.dumps({"bri": bri})
        return self.hue.put(self.hue.lights_url + '/' + self.light_id + '/state', state)

    def setCt(self, ct):
        if not Ct.MIN.value <= ct <= Ct.MAX.value:
            raise ValueError('ct must be int between ' + str(Ct.MIN.value) + ' and ' + str(Ct.MAX.value))

        state = json.dumps({"ct": ct})
        return self.hue.put(self.hue.lights_url + '/' + self.light_id + '/state', state)

    def setAlert(self, alert):
        if not isinstance(alert, Alert):
            raise TypeError('alert must be an instance of Alert Enum')

        state = json.dumps({"alert": alert.value})
        return self.hue.put(self.hue.lights_url + '/' + self.light_id + '/state', state)
