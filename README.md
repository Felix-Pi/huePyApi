# huePyApi
> Python module for controlling Philips Hue lights, groups, scenes and sensors by using the Hue rest API

### Installation
 `python3 -m pip install git+https://github.com/Felix-Pi/huePyApi`

## Configuration

#### manually (config.py)
```python
ip = ''
api_key = ''
```

## ToDo
**Testing** \
[ ] more testing, exceptions \
[ ] requests: error messages -> https://developers.meethue.com/develop/hue-api/error-messages/ \
[ ] requests http 

**Functions** \
[ ] change colors \
[ ] register new user / api key \
[ ] sensors, rules, schedules \
[ ] capabilities
[ ] read temperature from sensor \

**Resourcelinks** \
links: [Lights, Sensors, Groups, Scenes, Rules, Schedules, ResourceLinks]

**Other** \
[ ] maybe a GUI



## Usage
### Hue
```python
from huePyApi import Hue
from config import ip, api_key

hue = Hue.Hue(ip=ip, api_key=api_key)
```

### Groups
```python
groups = hue.get_all_groups()         # returns all groups
group = hue.get_group(<group_id>)     # returns group with id group_id


group.set_on(<state>)                 # (''| True) = on, False = off
group.set_bri(<brightness>)           # set brightness to value between 1 and 254
group.set_ct(<color temp>)            # set color temperature to value between 153 and 500
group.set_alert(Alert.LSELECT)        # alert effect (Alert.NONE|Alert.SELECT|Alert.LSELECT)

group_scenes = hue.get_scenes_for_group(group)     # returns scenes associated with group
group.set_scene(group_scenes[0])                   # sets scene group_scenes[0] in group
```

### Lights
```python
lights = hue.get_all_lights()        # returns all groups
light = hue.get_light(light_id)      # returns group with id group_id

light.set_on(<state>)                # (''| True) = on, False = off
light.set_bri(<brightness>)          # set brightness to value between 1 and 254
light.set_ct(<color temp>)           # set color temperature to value between 153 and 500
light.set_alert(Alert.SELECT)        # alert effect (Alert.NONE|Alert.SELECT|Alert.LSELECT)
```

### Scenes
```python
scenes = hue.get_all_scenes()         # returns all scenes
scene = hue.get_scene(<scene_id>)     # returns scene with id scene_id
```

### Resourcelinks
```python
resourcelinks = hue.get_all_resourcelinks()         # returns all resourcelinks
resourcelink = hue.get_resourcelink(<str>)          # returns resourcelink with id rl_id

resourcelink.get_linked_scenes()       # returns linked scenes
resourcelink.get_linked_rules()        # returns linked rules
resourcelink.get_linked_sensors()      # returns linked sensors
resourcelink.get_linked_groups()       # returns linked groups
```

### Sensors
```python
sensors = hue.get_all_sensors()         # returns all sensors
sensor = hue.get_sensor(<str>)          # returns sensor with id sensor_id

# sensor methods
sensor_id = sensor.get_sensor_id()
sensor_name = sensor.get_name()
sensor_type= sensor.get_sensor_type()
modelid = sensor.get_modelid()
lastupdated = sensor.get_lastupdated()
config_on = sensor.get_config_on()

# get sensors from model id
sensors = hue.get_sensors_for_modelid(<SensorModel>) # sensor models (SensorModel.HUE_DIMMER_SWITCH|SensorModel.HUE_MOTION_SENSOR|SensorModel.HUE_GEOFENCE)

# hue dimmer switch
hue_dimmer_switch = hue.get_sensors_for_modelid(SensorModel.HUE_DIMMER_SWITCH)
battery = hue_dimmer_switch.get_battery()
is_reachable = hue_dimmer_switch.is_reachable()

#hue motion sensor
hue_motion_sensor = hue.get_sensors_for_modelid(SensorModel.HUE_MOTION_SENSOR)[0]
#ToDo: sub sensors


#hue daylight sensor
hue_daylight_sensor = hue.get_sensors_for_modelid(SensorModel.HUE_DAYLIGHT_SENSOR)[0]

#hue geofence
hue_geofence = hue.get_sensors_for_modelid(SensorModel.HUE_GEOFENCE)[0]
presence = hue_geofence.get_presence()


#hue temparature sensor
temperature_sensor = self.hue.get_sensor(<sensor_id>)
temperature = temperature_sensor.get_temperature()              # returns temperature. format: xxxx
temperature = temperature_sensor.get_temperature_in_celsius()   # returns temperature in format: xx.xx
temperature = temperature_sensor.get_temperature_formatted()    # returns temparature in string with unit. format: xx.xx °C
```

## Credits
* hue api docs ([Hue API](https://developers.meethue.com/develop/hue-api/lights-api/))
