import enum


class SensorModel(enum.Enum):
    HUE_DIMMER_SWITCH = 'RWL021'
    HUE_MOTION_SENSOR = 'SML001'
    HUE_DAYLIGHT_SENSOR = 'PHDL00'
    HUE_GEOFENCE = 'HA_GEOFENCE'
    HUE_HOMEAWAY = 'HOMEAWAY'
    HUELABSENUM = 'HUELABSENUM' #ToDO: implement
    WAKEUP = 'WAKEUP' #ToDO: implement
    GOTOSLEEP = 'GOTOSLEEP' #ToDO: implement
