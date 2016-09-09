class Configuration:
    'This class represents a single configuration, build from traveloptions, for a request'

    @staticmethod
    def build(travelOptions):
        
        polygonJson = {
          "values": travelOptions.getTravelTimes(),
          "intersectionMode": travelOptions.getPolygonIntersectionMode().value,
          "serializer": travelOptions.getPolygonSerializationType().value,
          "pointReduction": True,
          "minPolygonHoleSize": travelOptions.getMinPolygonHoleSize()
        }

        if not travelOptions.getBufferMeter() is None:
            polygonJson['buffer'] = travelOptions.getBufferMeter();
        if not travelOptions.getSimplifyMeter() is None:
            polygonJson['simplify'] = travelOptions.getSimplifyMeter();
        if not travelOptions.getSrid() is None:
            polygonJson['srid'] = travelOptions.getSrid();
        if not travelOptions.getQuadrantSegments() is None:
            polygonJson['quadrantSegments'] = travelOptions.getQuadrantSegments();

        return {
            "sources": travelOptions.getSources(),
            "polygon" : polygonJson
        };