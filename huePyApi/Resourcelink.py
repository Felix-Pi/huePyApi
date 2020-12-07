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

    def parseLinkPattern(self, pattern):
        return [pattern.match(link).groups()[0] for link in self.links if pattern.match(link) is not None]

    def getLinkedScenes(self):
        scenes = self.parseLinkPattern(re.compile('/scenes/(.{15})'))
        return scenes

    def getLinkedRules(self):
        return self.parseLinkPattern(re.compile('/rules/(\w*)'))

    def getLinkedSensors(self):
        return self.parseLinkPattern(re.compile('/sensors/(\w*)'))

    def getLinkedGroups(self):
        return self.parseLinkPattern(re.compile('/groups/(\w*)'))
