# Anfrage parameter festlegen
params = {
    "outputFileName" : "augenaerzte_1800_car.gdb",
    "intersection"   : "union",
    "travelTimes"    : [900, 1800, 2700, 3600],
    "travelType"     : "car",
    "date"           : 20160701,
    "time"           : 43200,
    "frame"          : 14400,
    "walkSpeed"      : 4.5,
    "population"     : ["total_population"]
}

# quellen aus der punktwolke laden
sources : [
    { "id": "augenarzt_1", lat : , lng: },
    { "id": "augenarzt_1", lat : , lng: },
    ...
    { "id": "augenarzt_50", lat : , lng: }
]

# Anfrage an den LGB service
r = requests.get('https://service.route360.net/lgb/population', params=params, data=sources)
# Lesen des Requests
z = zipfile.ZipFile(io.BytesIO(r.content))
# Entpacken/Speichern des FileGDB Packets 
z.extractall("C:/Pfad/zum/Speichern")
