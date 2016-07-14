import json
from src.util.TravelOptions import TravelOptions
from src.rest.polygon.PolygonService import PolygonService
from src.util.enum.PolygonSerializationType import PolygonSerializationType
from src.util.enum.TravelType import TravelType

travelOptions = TravelOptions();
travelOptions.addSource({ "id": "id1", "lat" : 52.14, "lng" : 13.37, "tm" : { "bike" : {}}})
travelOptions.setServiceKey('uhWrWpUhyZQy8rPfiC7X')
travelOptions.setTravelTimes([200, 300])
travelOptions.setServiceUrl('https://service.route360.net/germany/')
travelOptions.setMinPolygonHoleSize(100000000)
travelOptions.setTravelType(TravelType.CAR)
# travelOptions.setPolygonSerializationType(PolygonSerializationType.JSON)
travelOptions.setPolygonSerializationType(PolygonSerializationType.GEOJSON)

polygonService = PolygonService()
polygon = polygonService.getPolygons(travelOptions)

# print(polygonService.getConfiguration(travelOptions))


f = open('data/sample.geojson', 'w')
f.write(json.dumps(polygon["data"]))