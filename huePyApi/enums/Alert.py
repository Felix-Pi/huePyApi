import enum


class Alert(enum.Enum):
    NONE = 'none' #he light is not performing an alert effect
    SELECT = 'select' #The light is performing one breathe cycle.
    LSELECT = 'lselect' #The light is performing breathe cycles for 15 seconds
