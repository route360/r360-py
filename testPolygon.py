import json
from src.util.TravelOptions import TravelOptions
from src.util.Configuration import Configuration
from src.rest.polygon.PolygonService import PolygonService
from src.util.enum.PolygonSerializationType import PolygonSerializationType
from src.util.enum.TravelType import TravelType

    # for travelType in ["walk", "car", "transit"]

for travelTime in [30 * 60, 60 * 60, 90 * 60]:
    for travelType in ["walk", "car", "transit"]:

        travelOptions = TravelOptions();
        travelOptions.addSource({ "id": str(travelTime) + travelType, "lat" : 52.52,  "lng" : 13.405, "tm" : { travelType : {
                "date" : 20160715, "time" : 36000
            }}})
        travelOptions.setServiceKey('uhWrWpUhyZQy8rPfiC7X')
        travelOptions.setTravelTimes([travelTime])
        travelOptions.setServiceUrl('https://service.route360.net/germany/')
        travelOptions.setMinPolygonHoleSize(100000000)
        # travelOptions.setTravelDate(20160715)
        # travelOptions.setTravelDate(36000)
        travelOptions.setTravelType(TravelType.parse(travelType))
        travelOptions.setPolygonSerializationType(PolygonSerializationType.GEOJSON)

        polygonService = PolygonService()
        polygon = polygonService.getPolygons(travelOptions)

        print(Configuration.build(travelOptions))

        filename = str(travelTime) + "_" + travelType + ".geojson"

        f = open('/Users/gerb/Development/workspaces/data/motionintelligence/clients/api/geojson/' + filename, 'w')
        f.write(json.dumps(polygon["data"]))