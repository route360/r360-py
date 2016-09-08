import json
import requests
import zipfile
import io

# Anfrage parameter festlegen
params = {
    "filename"       : "augenaerzte_1800_car.gdb",
    # "intersection"   : "union",
    "travelTimes"    : [900, 1800, 2700, 3600],
    "travelType"     : "CAR",
    # "date"           : 20160701,
    # "time"           : 43200,
    # "frame"          : 14400,
    # "walkSpeed"      : 4.5,
    "statistic"     : ["population_total"],
    "sources"        : json.dumps([
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5300, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5300, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5300, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5300, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5200, 'lng': 13.405 },
        { "id": "augenarzt_1", 'lat' : 52.5300, 'lng': 13.405 }
    ])
}

# https://dev.route360.net/lgb/population?sources=[{lat:52.15,lng:13.37,id=%22asd%22}]&travelTimes=900&travelType=CAR&statistic=population_total

# Anfrage an den LGB service
r = requests.get('https://dev.route360.net/lgb/population', params=params)

# print(r.url)
# print(r.content)

# # Lesen des Requests
z = zipfile.ZipFile(io.BytesIO(r.content))
# Entpacken/Speichern des FileGDB Packets 
z.extractall("/Volumes/DATA/Development/workspaces/data/motionintelligence/clients/lgb/results/filegdb/" + params['filename'])
