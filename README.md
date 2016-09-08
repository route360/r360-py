# r360-py - Python Library for the Route360° API

## API-Key
Get your API key [here ](https://developers.route360.net/apikey.html).

## Installation
Install this library easily via PIP:

    pip install r360_py

## Usage
      usage: getPolygons.py [-h] [--serviceUrl SERVICEURL] [--serviceKey SERVICEKEY]
                          [--travelType TRAVELTYPE]
                          [--travelTimes TRAVELTIMES [TRAVELTIMES ...]]
                          [--time TIME] [--date DATE]
                          [--polygonSerializer POLYGONSERIALIZER]
                          [--source SOURCE] [--outputDir OUTPUTDIR]
                          [--outputFilename OUTPUTFILENAME]
    
    Query the Route360° Polygon service in python
    
    optional arguments:
      -h, --help            show this help message and exit
      --serviceUrl SERVICEURL
                            The URL of the Route360° API endpoint.
      --serviceKey SERVICEKEY
                            Your personal key for the API.
      --travelType TRAVELTYPE
                            The travel type for the request: car, walk, bike or
                            transit
      --travelTimes TRAVELTIMES [TRAVELTIMES ...]
                            The travel time in seconds as a list of integers.
      --time TIME           The time in seconds of the day: 1.30 p.m. = 13 * 3600
                            + 30 * 60 = 48600 (transit only)
      --date DATE           The date in the format YYYYMMDD, e.g.: 20160727 for
                            the 27th of July 2016 (transit only)
      --polygonSerializer POLYGONSERIALIZER
                            The serializer for the polygons: json or geojson
      --source SOURCE       The source as doubles (lat,lng) separated by ';'.
      --outputDir OUTPUTDIR
                            The path where to write the output files
      --outputFilename OUTPUTFILENAME
                            The the name of the file to write to   

### Example

    py getPolygons.py --travelType walk \
                   --travelTime 1800 \
                   --source "52.52;13.405" \
                   --outputDir data/ \
                   --outputFilename test.geojson \
                   --serviceKey 'Your key here' \
                   --serviceUrl http://service.route360.net/germany/


### Update
    
    http://peterdowns.com/posts/first-time-with-pypi.html

    git tag 0.1 -m ""
    git push --tags origin 
    python setup.py register -r pypitest
    python setup.py sdist upload -r pypitest
    python setup.py register -r pypi
    python setup.py sdist upload -r pypi