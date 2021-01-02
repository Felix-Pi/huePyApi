from huePyApi.enums.SensorModel import SensorModel
from huePyApi.enums.SensorType import SensorType


def parse_sensor(hue, sensor_id, sensor):
    # print('parseSensor:', sensor)
    name = sensor['name']
    sensor_type = sensor['type']
    modelid = sensor['modelid']
    lastupdated = sensor['state']['lastupdated']
    config = sensor['config']

    # HUE_MOTION_SENSOR
    if modelid == SensorModel.HUE_MOTION_SENSOR.value:

        if sensor_type == SensorType.HUE_MOTION_SENSOR_LIGHT_LEVEL.value:
            lightlevel = sensor['state']['lightlevel']
            dark = sensor['state']['dark']
            daylight = sensor['state']['daylight']
            return LightLevelSensor(hue, sensor_id, name, sensor_type, modelid, lastupdated, config, lightlevel,
                                    dark,
                                    daylight)

        if sensor_type == SensorType.HUE_MOTION_SENSOR_PRESENCE.value:
            presence = sensor['state']['presence']
            return PresenceSensor(hue, sensor_id, name, sensor_type, modelid, lastupdated, config, presence)

        if sensor_type == SensorType.HUE_MOTION_SENSOR_TEMPERATURE.value:
            temperature = sensor['state']['temperature']
            return TemperatureSensor(hue, sensor_id, name, sensor_type, modelid, lastupdated, config, temperature)

    # HUE_DIMMER_SWITCH
    if modelid == SensorModel.HUE_DIMMER_SWITCH.value:
        return DimmerSwitch(hue, sensor_id, name, sensor_type, modelid, lastupdated, config)

    # HUE_GEOFENCE
    if modelid == SensorModel.HUE_GEOFENCE.value:
        presence = sensor['state']['presence']
        return Geofence(hue, sensor_id, name, sensor_type, modelid, lastupdated, config, presence)

    # HUE_GEOFENCE
    if modelid == SensorModel.HUE_DAYLIGHT_SENSOR.value:
        daylight = sensor['state']['daylight']
        return DaylightSensor(hue, sensor_id, name, sensor_type, modelid, lastupdated, config, daylight)

    return Sensor(hue, sensor_id, name, sensor_type, modelid, lastupdated, config)


class Sensor:
    def __init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config):
        self.hue = hue
        self.sensor_id = str(sensor_id)
        self.name = str(name)
        self.sensor_type = str(sensor_type)
        self.modelid = modelid
        self.lastupdated = lastupdated
        self.config = config

    def __repr__(self):
        return '{} (id={}, name={}, type={}, modelid={}, lastupdated={}, config={})'.format(
            self.__class__.__name__,
            self.sensor_id, self.name,
            self.sensor_type,
            self.modelid,
            self.lastupdated,
            self.config)

    def get_sensor_id(self):
        return self.sensor_id

    def get_name(self):
        return self.name

    def get_sensor_type(self):
        return self.sensor_type

    def get_modelid(self):
        return self.modelid

    def get_lastupdated(self):
        return self.lastupdated

    def get_config_on(self):
        return bool(self.config['on'])


class DimmerSwitch(Sensor):
    def __init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config):
        Sensor.__init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config)

    def __repr__(self):
        return Sensor.__repr__(self)

    def get_battery(self):
        return int(self.config['battery'])

    def is_reachable(self):
        return bool(self.config['reachable'])


class HueMotionSensor(Sensor):
    def __init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config):
        Sensor.__init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config)

    def get_battery(self):
        return int(self.config['battery'])

    def get_alert(self):
        return self.config['alert']

    def is_usertest(self):
        return bool(self.config['usertest'])

    def is_on(self):
        return bool(self.config['on'])

    def get_ledindication(self):
        return bool(self.config['ledindication'])


class PresenceSensor(HueMotionSensor):
    def __init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config, presence):
        HueMotionSensor.__init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config)
        self.presence = bool(presence)

    def __repr__(self):
        return HueMotionSensor.__repr__(self)

    def get_presence(self):
        return self.presence

    def get_sensitivity(self):
        return self.config['sensitivity']

    def get_sensitivitymax(self):
        return self.config['sensitivitymax']


class LightLevelSensor(HueMotionSensor):
    def __init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config, lightlevel, dark, daylight):
        HueMotionSensor.__init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config)
        self.lightlevel = int(lightlevel)
        self.dark = bool(dark)
        self.daylight = bool(daylight)

    def get_light_level(self):
        return self.lightlevel

    def get_dark(self):
        return self.lightlevel

    def get_daylight(self):
        return self.lightlevel

    def get_tholddark(self):
        return self.config['tholddark']

    def get_tholdoffset(self):
        return self.config['tholdoffset']

    def __repr__(self):
        return HueMotionSensor.__repr__(self)[:-1] + ', lightlevel={}, dark={}, daylight={})'.format(self.lightlevel,
                                                                                                     self.dark,
                                                                                                     self.daylight)


class TemperatureSensor(HueMotionSensor):
    def __init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config, temperature):
        HueMotionSensor.__init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config)
        self.temperature = int(temperature)

    def __repr__(self):
        return HueMotionSensor.__repr__(self)[:-1] + ', temperature={})'.format(self.temperature)

    def get_temperature(self):
        return self.temperature

    def get_temperature_in_celsius(self):
        return self.temperature / 100

    def get_temperature_formatted(self):
        return '{} °C'.format(self.temperature / 100)


class Geofence(Sensor):
    def __init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config, presence):
        Sensor.__init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config)
        self.presence = bool(presence)

    def __repr__(self):
        return Sensor.__repr__(self)[:-1] + ', presence={})'.format(self.presence)

    def get_presence(self):
        return bool(self.presence)


class DaylightSensor(Sensor):
    def __init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config, daylight):
        Sensor.__init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config)
        self.daylight = bool(daylight)

    def __repr__(self):
        return Sensor.__repr__(self)[:-1] + ', daylight={})'.format(self.daylight)

    def get_daylight(self):
        return bool(self.daylight)

    def get_sunriseoffset(self):
        return self.config['sunriseoffset']

    def get_sunsetoffset(self):
        return self.config['sunsetoffset']
