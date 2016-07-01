import json
import requests
import urllib.parse

class PolygonService:
    'This class should be used to query the polygon service'

    def __init__(self):
        return

    def getConfiguration(self, travelOptions):
        
        cfg = {
            "sources": travelOptions.getSources(),
            "polygon": {
              "values": [ 300, 600, 900, 1200, 1500, 1800],
              "intersectionMode": "union",
              "serializer": travelOptions.getPolygonSerializationType().value,
              "pointReduction": True,
              "minPolygonHoleSize": 1000000
            }
        }

        return cfg;

    def getPolygons(self, travelOptions):

        params = {
            "key" : travelOptions.getServiceKey(),
            "cfg" : json.dumps(self.getConfiguration(travelOptions))
        }

        r = requests.get(travelOptions.getServiceUrl() + 'v1/polygon', params=params)

        return json.loads(r.text)
