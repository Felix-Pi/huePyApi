# ToDo: read temperature from motion sensor

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


class Geofence(Sensor):
    def __init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config, presence):
        Sensor.__init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config)
        self.presence = bool(presence)

    def __repr__(self):
        return Sensor.__repr__(self)[:-1] + ', presence={})'.format(self.presence)

    def get_presence(self):
        return self.presence


class DimmerSwitch(Sensor):
    def __init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config):
        Sensor.__init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, config)

    def __repr__(self):
        return Sensor.__repr__(self)

    def get_battery(self):
        return int(self.config['battery'])

    def is_reachable(self):
        return bool(self.config['reachable'])
