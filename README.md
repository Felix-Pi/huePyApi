# huePyApi
> Python module for controlling Philips Hue lights, groups, scenes and sensors by using the Hue rest API

### Installation
 `pip install git+https://github.com/Felix-Pi/huePyApi`

## Configuration

#### manually (config.py)
```
ip = ''
api_key = ''
```

## Usage
### Hue
```python
from huePyApi import Hue
from config import ip, api_key

hue = Hue.Hue(ip=ip, api_key=api_key)
```

### Groups
```python
groups = hue.getAllGroups()          # returns all groups
group = hue.getGroup(<group_id>)     # returns group with id group_id


group.setOn(<state>)                 # (''| True) = on, False = off
group.setBri(<brightness>)           # set brightness to value between 1 and 254
group.setAlert(Alert.LSELECT)        # alert effect, (Alert.NONE|Alert.SELECT|Alert.LSELECT)

group_scenes = hue.getScenesForGroup(group)     # returns scenes associated with group
group.setScene(group_scenes[0])                 # sets scene group_scenes[0] in group
```

### Lights
```python
lights = hue.getAllLights()         # returns all groups
light = hue.getLight(light_id)      # returns group with id group_id

light.setOn(<state>)                # (''| True) = on, False = off
light.setBri(<brightness>)          # set brightness to value between 1 and 254
light.setAlert(Alert.SELECT)        # alert effect, (Alert.NONE|Alert.SELECT|Alert.LSELECT)
```

### Scenes
```python
scenes = hue.getAllScenes()         # returns all scenes
scene = hue.getScene(<scene_id>)    # returns scene with id scene_id
```

### Resourcelinks
```python
resourcelinks = hue.getAllResourcelinks()         # returns all resourcelinks
resourcelink = hue.getResourcelink(<str>)         # returns resourcelink with id rl_id

resourcelink.getLinkedScenes()       # returns linked scenes
resourcelink.getLinkedRules()        # returns linked rules
resourcelink.getLinkedSensors()      # returns linked sensors
resourcelink.getLinkedGroups()       # returns linked groups

```
