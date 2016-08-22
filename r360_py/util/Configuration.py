class Configuration:
    'This class represents a single configuration, build from traveloptions, for a request'

    @staticmethod
    def build(travelOptions):
        
        return {
            "sources": travelOptions.getSources(),
            "polygon": {
              "values": travelOptions.getTravelTimes(),
              "intersectionMode": "union",
              "serializer": travelOptions.getPolygonSerializationType().value,
              "pointReduction": True,
              "minPolygonHoleSize": 1000000
            }
        };