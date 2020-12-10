import enum


class SensorType(enum.Enum):
    HUE_MOTION_SENSOR_LIGHT_LEVEL = 'ZLLLightLevel'
    HUE_MOTION_SENSOR_TEMPERATURE = 'ZLLTemperature'
    HUE_MOTION_SENSOR_PRESENCE = 'ZLLPresence'
    HUE_SWITCH = 'ZLLSwitch'
