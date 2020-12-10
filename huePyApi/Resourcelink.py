# currently used to get nformation (especially scenes) from Hue Dimmer Switch
# "classid": 10013 --> Hue Dimmer Switch

import re


class Resourcelink:
    def __init__(self, hue, rl_id, classid, description, name, links):
        self.hue = hue
        self.group_id = rl_id
        self.classid = classid
        self.description = description
        self.name = name
        self.links = links

    def __repr__(self):
        return 'Resourcelink(id={}, classid={}, description={}, name={}, links={})'.format(self.group_id,
                                                                                           self.classid,
                                                                                           self.description,
                                                                                           self.name,
                                                                                           self.links)

    def parse_link_pattern(self, pattern):
        return [pattern.match(link).groups()[0] for link in self.links if pattern.match(link) is not None]

    def get_linked_scenes(self):
        scenes = self.parse_link_pattern(re.compile('/scenes/(.{15})'))
        return scenes

    def get_linked_rules(self):
        return self.parse_link_pattern(re.compile('/rules/(\w*)'))

    def get_linked_sensors(self):
        return self.parse_link_pattern(re.compile('/sensors/(\w*)'))

    def get_linked_groups(self):
        return self.parse_link_pattern(re.compile('/groups/(\w*)'))
