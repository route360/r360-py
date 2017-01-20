from r360_py.util.Util import Util
from r360_py.util.enum.EdgeWeightType import EdgeWeightType
from r360_py.util.enum.PathSerializerType import PathSerializerType
from r360_py.util.enum.PolygonIntersectionMode import PolygonIntersectionMode

class TravelOptions:
    'This class represents the configuration for one request'

    def __init__(self):
        self.sources = []
        self.targets = []
        self.travelTimes = []
        self.travelType = None
        self.buffer = None
        self.simplifyMeter = None
        self.quadrantSegments = None
        self.srid = None
        self.travelDate = Util.currentDate()
        self.travelTime = Util.currentTime()
        self.minPolygonHoleSize = 100000000
        self.intersectionMode = PolygonIntersectionMode.UNION
        self.polygonSerializationType = None
        self.pathSerializer = PathSerializerType.COMPACT_PATH_SERIALIZER
        self.edgeWeightType = EdgeWeightType.TIME

    def setPolygonSerializationType(self, polygonSerializationType):
        self.polygonSerializationType = polygonSerializationType

    def getPolygonSerializationType(self):
        return self.polygonSerializationType

    def setServiceUrl(self, serviceUrl):
        self.serviceUrl = serviceUrl

    def getServiceUrl(self):
        return self.serviceUrl

    def setServiceKey(self, serviceKey):
        self.serviceKey = serviceKey

    def getServiceKey(self):
        return self.serviceKey

    def setSources(self, sources):
        self.sources = sources

    def getSources(self):
        return self.sources

    def addSource(self, source):
        self.sources.append(source)

    def setTargets(self, targets):
        self.targets = targets

    def getTargets(self):
        return self.targets

    def addTarget(self, target):
        self.targets.append(target)

    def setTravelTimes(self, travelTimes):
        self.travelTimes = travelTimes;

    def getTravelTimes(self):
        return self.travelTimes;

    def addTravelTime(self, travelTime):
        self.travelTimes.append(source)

    def setMinPolygonHoleSize(self, minPolygonHoleSize):
        self.minPolygonHoleSize = minPolygonHoleSize

    def getMinPolygonHoleSize(self):
        return self.minPolygonHoleSize

    def setTravelType(self, travelType):
        self.travelType = travelType

    def getTravelType(self):
        return self.travelType

    def setTravelTime(self, travelTime):
        self.travelTime = travelTime

    def getTravelTime(self):
        return self.travelTime

    def setTravelDate(self, travelDate):
        self.travelDate = travelDate

    def getTravelDate(self):
        return self.travelDate

    def setPolygonIntersectionMode(self, intersectionMode):
        self.intersectionMode = intersectionMode

    def getPolygonIntersectionMode(self):
        return self.intersectionMode

    def setBuffer(self, buffer):
        self.buffer = buffer

    def getBuffer(self):
        return self.buffer

    def setSimplifyMeter(self, simplifyMeter):
        self.simplifyMeter = simplifyMeter

    def getSimplifyMeter(self):
        return self.simplifyMeter

    def setQuadrantSegments(self, quadrantSegments):
        self.quadrantSegments = quadrantSegments

    def getQuadrantSegments(self):
        return self.quadrantSegments

    def setSrid(self, srid):
        self.srid = srid

    def getSrid(self):
        return self.srid

    def setPathSerializer(self, path_serializer):
        self.pathSerializer = path_serializer

    def getPathSerializer(self):
        return self.pathSerializer

    def getEdgeWeightType(self):
        return self.edgeWeightType

    def setEdgeWeightType(self, edge_weight_type):
        self.edgeWeightType = edge_weight_type
