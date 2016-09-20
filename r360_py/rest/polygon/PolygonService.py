import json
import requests
import urllib.parse
from r360_py.util.Configuration import Configuration

class PolygonService:
    'This class should be used to query the polygon service'

    def __init__(self):
        return

    def getPolygons(self, travelOptions):

        params = {
            "key" : travelOptions.getServiceKey(),
            "cfg" : json.dumps(Configuration.build(travelOptions))
        }

        r = requests.get(travelOptions.getServiceUrl() + 'v1/polygon', params=params)

        if ( r.status_code == 403 ):
            raise PermissionError(r.text)

        return json.loads(r.text)
