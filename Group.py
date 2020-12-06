import json


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
        self.hue.put(self.hue.groups_url + '/' + str(self.group_id) + '/action', state)

    def setBri(self, bri):
        state = json.dumps({"bri": bri})
        self.hue.put(self.hue.groups_url + '/' + str(self.group_id) + '/action', state)

    def setAlert(self, alert):
        state = json.dumps({"alert": alert})
        self.hue.put(self.hue.groups_url + '/' + str(self.group_id) + '/action', state)

    def setScene(self, scene):
        self.setSceneById(scene.scene_id)

    def setSceneById(self, scene_id):
        state = json.dumps({"scene": scene_id})
        self.hue.put(self.hue.groups_url + '/' + str(self.group_id) + '/action', state)