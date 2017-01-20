class Configuration:
    'This class represents a single configuration, build from traveloptions, for a request'

    @staticmethod
    def build(travelOptions):
        cfg = {
            "sources": travelOptions.getSources()
        }

        if travelOptions.getTravelTimes():
            polygonJson = {
              "values": travelOptions.getTravelTimes(),
              "intersectionMode": travelOptions.getPolygonIntersectionMode().value,
              "serializer": travelOptions.getPolygonSerializationType().value,
              "pointReduction": True,
              "minPolygonHoleSize": travelOptions.getMinPolygonHoleSize()
            }

            if not travelOptions.getBuffer() is None:
                polygonJson['buffer'] = travelOptions.getBuffer();
            if not travelOptions.getSimplifyMeter() is None:
                polygonJson['simplify'] = travelOptions.getSimplifyMeter();
            if not travelOptions.getSrid() is None:
                polygonJson['srid'] = travelOptions.getSrid();
            if not travelOptions.getQuadrantSegments() is None:
                polygonJson['quadrantSegments'] = travelOptions.getQuadrantSegments();

            cfg['polygon'] = polygonJson

        if not travelOptions.getPathSerializer() is None:
            cfg['pathSerializer'] = travelOptions.getPathSerializer().value

        if travelOptions.getTargets():
            cfg['targets'] = travelOptions.getTargets()

        if not travelOptions.getEdgeWeightType() is None:
            cfg['edgeWeightType'] = travelOptions.getEdgeWeightType().value

        return cfg
