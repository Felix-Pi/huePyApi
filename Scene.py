class Scene:
    def __init__(self, hue, scene_id, name, group, lights, lightstates):
        self.hue = hue
        self.scene_id = scene_id
        self.name = name
        self.group = group
        self.lights = lights
        self.lightstates = lightstates

    def __repr__(self):
        return 'Scene(id={}, name={}, group={}, lights={}, lightstates={})'.format(self.scene_id, self.name, self.group,
                                                                                   self.lights,
                                                                                   self.lightstates)
