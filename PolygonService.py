import json
import requests
import urllib.parse

cfg = {
    "sources": [
        {
            "lat": 52.516221,
            "lng": 13.386154,
            "id": "",
            "tm": {
                "bike": {}
            }
        }
    ],
    "polygon": {
      "values": [ 300, 600, 900, 1200, 1500, 1800],
      "intersectionMode": "union",
      "serializer": "json",
      "pointReduction": True,
      "minPolygonHoleSize": 1000000
    }
}

params = {
    "key" : "uhWrWpUhyZQy8rPfiC7X",
    "cfg" : json.dumps(cfg)
}

r = requests.get('https://service.route360.net/germany/v1/polygon', params=params)
print(r.url)
print(r.text)
