import json
from src.util.TravelOptions import TravelOptions
from src.rest.polygon.PolygonService import PolygonService
from src.util.enum.PolygonSerializationType import PolygonSerializationType

travelOptions = TravelOptions();


travelOptions.addSource({ "id": "id1", "lat" : 52.14, "lng" : 13.37, "tm" : { "bike" : {}}})
travelOptions.setServiceKey('uhWrWpUhyZQy8rPfiC7X')
travelOptions.setServiceUrl('https://service.route360.net/germany/')
travelOptions.setPolygonSerializationType(PolygonSerializationType.GEOJSON)

polygonService = PolygonService()

print(polygonService.getConfiguration(travelOptions))

polygon = polygonService.getPolygons(travelOptions)

f = open('data/sample.geojson', 'w')
f.write(json.dumps(polygon["data"]))