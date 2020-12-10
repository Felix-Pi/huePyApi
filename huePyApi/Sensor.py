# ToDo: read temperature from motion sensor

class Sensor:
    def __init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated):
        self.hue = hue
        self.sensor_id = str(sensor_id)
        self.name = str(name)
        self.sensor_type = str(sensor_type)
        self.modelid = modelid
        self.lastupdated = lastupdated

    def __repr__(self):
        return 'Sensor(id={}, name={}, type={}, modelid={}, lastupdated={})'.format(self.sensor_id, self.name,
                                                                                    self.sensor_type,
                                                                                    self.lastupdated,
                                                                                    self.modelid)

    def getSensorId(self):
        return self.sensor_id

    def getName(self):
        return self.name

    def getSensorType(self):
        return self.sensor_type

    def getModelid(self):
        return self.modelid

    def getLastupdated(self):
        return self.lastupdated


class PresenceSensor(Sensor):
    def __init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, presence):
        Sensor.__init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated)
        self.presence = bool(presence)

    def __repr__(self):
        return 'PresenceSensor(id={}, name={}, type={}, modelid={}, lastupdated={}, presence={})'.format(self.sensor_id,
                                                                                                         self.name,
                                                                                                         self.sensor_type,
                                                                                                         self.modelid,
                                                                                                         self.lastupdated,
                                                                                                         self.presence)

    def getPresence(self):
        return self.presence


class LightLevelSensor(Sensor):
    def __init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, lightlevel, dark, daylight):
        Sensor.__init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated)
        self.lightlevel = int(lightlevel)
        self.dark = bool(dark)
        self.daylight = bool(daylight)

    def getLightLevel(self):
        return self.lightlevel

    def getDark(self):
        return self.lightlevel

    def getDaylight(self):
        return self.lightlevel

    def __repr__(self):
        return 'LightLevelSensor(id={}, name={}, type={}, modelid={}, lastupdated={}, lightlevel={}, dark={}, daylight={})'.format(
            self.sensor_id, self.name,
            self.sensor_type, self.modelid,
            self.lastupdated,
            self.lightlevel,
            self.dark,
            self.daylight)


class TemperatureSensor(Sensor):
    def __init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated, temperature):
        Sensor.__init__(self, hue, sensor_id, name, sensor_type, modelid, lastupdated)
        self.temperature = int(temperature)

    def __repr__(self):
        return 'TemperatureSensor(id={}, name={}, type={}, modelid={}, lastupdated={}, temperature={})'.format(
            self.sensor_id,
            self.name,
            self.sensor_type,
            self.modelid,
            self.lastupdated,
            self.temperature)

    def getTemperature(self):
        return self.temperature
