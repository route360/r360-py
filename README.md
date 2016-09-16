# r360-py - Python Library for the Route360° API

## API-Key
Get your API key [here ](https://developers.route360.net/apikey.html).

## Installation
Install this library easily via PIP:

    pip install r360_py
    
If you have multiple version of Python installed, make sure you are using the correct version:

    /usr/local/bin/pip3.5 install r360_py

## Usage
    Usage: getPolygons.py [-h] [--serviceUrl SERVICEURL] [--serviceKey SERVICEKEY]
                      [--travelType TRAVELTYPE]
                      [--travelTimes TRAVELTIMES [TRAVELTIMES ...]]
                      [--time TIME] [--date DATE]
                      [--polygonSerializer POLYGONSERIALIZER]
                      [--source SOURCE] [--buffer BUFFER]
                      [--simplify SIMPLIFY] [--srid SRID]
                      [--quadrantSegments QUADRANTSEGMENTS]
                      [--outputDir OUTPUTDIR]
                      [--outputFilename OUTPUTFILENAME]

    Query the Route360° Polygon service in python

    optional arguments:
      -h, --help            show this help message and exit
      --serviceUrl SERVICEURL
                            The URL of the Route360° API endpoint. (default: None)
      --serviceKey SERVICEKEY
                            Your personal key for the API. (default: None)
      --travelType TRAVELTYPE
                            The travel type for the request: car, walk, bike or
                            transit (default: None)
      --travelTimes TRAVELTIMES [TRAVELTIMES ...]
                            The travel time in seconds as a list of integers.
                            (default: None)
      --time TIME           The time in seconds of the day: 1.30 p.m. = 13 * 3600
                            + 30 * 60 = 48600 (transit only) (default: 43200)
      --date DATE           The date in the format YYYYMMDD, e.g.: 20160727 for
                            the 27th of July 2016 (transit only) (default:
                            20162707)
      --polygonSerializer POLYGONSERIALIZER
                            The serializer for the polygons: json or geojson
                            (default: geojson)
      --source SOURCE       The source as doubles (lat,lng) separated by ';'.
                            (default: None)
      --buffer BUFFER       The buffer (in meter) that should be generated around
                            the polygons. (max 500m) (default: None)
      --simplify SIMPLIFY   The threshold (in meter) that should be used for
                            Douglas-Puecker (before buffering, max 500m).
                            (default: None)
      --srid SRID           The target SRID (Spatial Reference System Identifier),
                            all that are supported via PostGIS. (default: None)
      --quadrantSegments QUADRANTSEGMENTS
                            The number of quadrant segements (max 8), see:
                            http://postgis.net/docs/ST_Buffer.html. (default:
                            None)
      --outputDir OUTPUTDIR
                            The path where to write the output files (default:
                            None)
      --outputFilename OUTPUTFILENAME
                            The the name of the file to write to (default: None)  

### Example

    python getPolygons.py --travelType walk \
                   --travelTime 1800 \
                   --source "52.52;13.405" \
                   --outputDir data/ \
                   --outputFilename test.geojson \
                   --serviceKey 'Your key here' \
                   --serviceUrl http://service.route360.net/germany/ \
                   --buffer 500 \
                   --simplify 200 \
                   --quadrantSegments 2 \
                   --srid 4326 \
