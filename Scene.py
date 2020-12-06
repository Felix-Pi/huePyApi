class Scene:
    def __init__(self, id, name, group, lights, lightstates):
        self.id = id
        self.name = name
        self.on = group
        self.bri = lights
        self.ct = lightstates
