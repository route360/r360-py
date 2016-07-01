class TravelOptions:
    'This class represents the configuration for one request'

    def __init__(self):
        self.sources = []

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
