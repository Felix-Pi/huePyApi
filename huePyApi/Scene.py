def parse_scene(hue, scene_id, scene):
    # print('parseScene:', scene)
    name = scene['name']

    group = None
    if 'group' in scene:
        group = scene['group']

    lights = scene['lights']
    lightstates = None
    if 'lightstates' in scene:
        lightstates = scene['lightstates']

    return Scene(hue, scene_id, name, group, lights, lightstates)


class Scene:
    def __init__(self, hue, scene_id, name, group, lights, lightstates):
        self.hue = hue
        self.scene_id = str(scene_id)
        self.name = str(name)
        self.group = str(group)
        self.lights = lights
        self.lightstates = lightstates

    def __repr__(self):
        return 'Scene(id={}, name={}, group={}, lights={}, lightstates={})'.format(self.scene_id, self.name, self.group,
                                                                                   self.lights,
                                                                                   self.lightstates)
