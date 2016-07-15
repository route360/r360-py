class TravelOptions:
    'This class represents the configuration for one request'

    def __init__(self):
        self.sources = []
        self.travelTimes = []
        self.minPolygonHoleSize = 100000000

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

    def setTravelTimes(self, travelTimes):
        self.travelTimes = travelTimes;

    def getTravelTimes(self):
        return self.travelTimes;

    def addTravelTime(self, travelTime):
        self.travelTimes.append(source)

    def setMinPolygonHoleSize(self, minPolygonHoleSize):
        self.minPolygonHoleSize = minPolygonHoleSize

    def getMinPolygonHoleSize():
        return self.minPolygonHoleSize

    def setTravelType(self, travelType):
        self.travelType = travelType

    def getTravelType():
        return self.travelType

    def setTravelTime(self, travelTime):
        self.travelTime = travelTime

    def getTravelTime():
        return self.travelTime

    def setTravelDate(self, travelDate):
        self.travelDate = travelDate

    def getTravelDate():
        return self.travelDate
