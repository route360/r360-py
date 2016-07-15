from enum import Enum

class TravelType(Enum):
    CAR = "car"
    WALK = "walk"
    BIKE = "bike"
    TRANSIT = "transit"

    @classmethod
    def parse(clazz, str):
      return getattr(clazz, str.upper(), None)