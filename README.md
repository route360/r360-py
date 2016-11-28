# r360-py - Python Library for the Route360° API

## API-Key
Get your API key [here ](https://developers.route360.net/apikey.html).

## Installation
### the r360-py library uses python3
make sure this is installed on your system
### use virtualenv for a clean, global-free install
[virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) is great. We can use it to sandbox versions and keep installs contained, so we can avoid global version conflicts.

Install virtualenv
```
pip install virtualenv
```

Create python3 virtualenv named 'venv'
```
virtualenv -p python3 venv
```

Activate virtualenv
```
source venv/bin/activate
```
_do this every time to enter into virtualenv called '(venv)' <= as shown in terminal prompt_

Install r360-py
```
pip install r360_py
```
*this installs r360_py and dependencies in our virtualenv*

Test the install
`python -m r360_py.cli -h` _this shows the cli usage and help_

When you are done using the virtualenv, shut it down
```
deactivate
```
_prompt drops '(venv)' tag, virtualenv is no longer active_

## Usage
    usage: r360_py.cli [-h] [--time TIME] [--date DATE]
                       [--polygonSerializer POLYGONSERIALIZER] [--buffer BUFFER]
                       [--simplify SIMPLIFY] [--srid SRID]
                       [--quadrantSegments QUADRANTSEGMENTS] --travelTimes
                       TRAVELTIMES [TRAVELTIMES ...] --serviceUrl SERVICEURL
                       --serviceKey SERVICEKEY --travelType TRAVELTYPE --source
                       SOURCE --outputDir OUTPUTDIR --outputFilename
                       OUTPUTFILENAME

    Query the Route360 Polygon service with python

    optional arguments:
      -h, --help            show this help message and exit
      --time TIME           The time in seconds of the day: 1.30 p.m. = 13 * 3600
                            + 30 * 60 = 48600 (transit only) (default: 43200)
      --date DATE           The date in the format YYYYMMDD, e.g.: 20160727 for
                            the 27th of July 2016 (transit only) (default:
                            20162707)
      --polygonSerializer POLYGONSERIALIZER
                            The serializer for the polygons: json or geojson
                            (default: geojson)
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

    required named arguments:
      --travelTimes TRAVELTIMES [TRAVELTIMES ...]
                            The travel time in seconds as a list of integers.
                            (default: None)
      --serviceUrl SERVICEURL
                            The URL of the Route360° API endpoint. (default: None)
      --serviceKey SERVICEKEY
                            Your personal key for the API. (default: None)
      --travelType TRAVELTYPE
                            The travel type for the request: car, walk, bike or
                            transit (default: None)
      --source SOURCE       The source as doubles (lat,lng) separated by ';'.
                            (default: None)
      --outputDir OUTPUTDIR
                            The path where to write the output files (default:
                            None)
      --outputFilename OUTPUTFILENAME
                            The the name of the file to write to (default: None)


### Example

    python -m r360_py.cli --travelType walk \
                   --travelTimes 1800 \
                   --source "52.52;13.405" \
                   --outputDir data/ \
                   --outputFilename test.geojson \
                   --serviceKey 'Your key here' \
                   --serviceUrl http://service.route360.net/germany/ \
                   --buffer 500 \
                   --simplify 200 \
                   --quadrantSegments 2 \
                   --srid 4326 \
