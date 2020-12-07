import json


class Light:
    def __init__(self, hue, light_id, name, on, bri, ct, alert):
        self.hue = hue
        self.light_id = str(light_id)
        self.name = str(name)
        self.on = bool(on)
        self.bri = int(bri)
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
        self.hue.put(self.hue.lights_url + '/' + str(self.light_id) + '/state', state)

    def setBri(self, bri):
        state = json.dumps({"bri": bri})
        self.hue.put(self.hue.lights_url + '/' + str(self.light_id) + '/state', state)

    def setAlert(self, alert):
        state = json.dumps({"alert": alert})
        self.hue.put(self.hue.lights_url + '/' + str(self.light_id) + '/state', state)
