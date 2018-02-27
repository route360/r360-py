# r360-py - Python Library for the Route360° API

## API-Key
Get your API key [here ](https://developers.route360.net/pricing/).

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
    usage: python -m r360_py.cli [-h] [--time TIME] [--date DATE]
                                 [--polygonSerializer POLYGONSERIALIZER]
                                 [--buffer BUFFER] [--minHoleSize MINHOLESIZE]
                                 [--simplify SIMPLIFY] [--srid SRID]
                                 [--quadrantSegments QUADRANTSEGMENTS]
                                 [--frameDuration FRAMEDURATION]
                                 [--reverse REVERSE] [--bikeSpeed BIKESPEED]
                                 [--bikeUphill BIKEUPHILL]
                                 [--bikeDownhill BIKEDOWNHILL]
                                 [--walkSpeed WALKSPEED] [--walkUphill WALKUPHILL]
                                 [--walkDownhill WALKDOWNHILL] --travelTimes
                                 TRAVELTIMES [TRAVELTIMES ...] --serviceUrl
                                 SERVICEURL --serviceKey SERVICEKEY --travelType
                                 TRAVELTYPE --source SOURCE --outputDir OUTPUTDIR
                                 --outputFilename OUTPUTFILENAME

    Query the Route360 Polygon service using python

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
        --buffer BUFFER       The buffer (in srid units) that should be generated
                              around the polygons. (default: None)
        --minHoleSize MINHOLESIZE
                              The area threshold of a hole inside a polygon (in
                              meters squared). (default: None)
        --simplify SIMPLIFY   The threshold (in meter) that should be used for
                              Douglas-Peucker (before buffering, max 500m).
                              (default: None)
        --srid SRID           The target SRID (Spatial Reference System Identifier),
                              all that are supported via PostGIS. (default: None)
        --quadrantSegments QUADRANTSEGMENTS
                              The number of quadrant segments (max 8), see:
                              http://postgis.net/docs/ST_Buffer.html. (default:
                              None)
        --frameDuration FRAMEDURATION
                              The window (in seconds) during which connections are
                              identified. (default: None)
        --reverse REVERSE     Whether or not to measure from sources (default) or
                              towards sources. (default: None)
        --bikeSpeed BIKESPEED
                              Bike speed km/h (travelType 'bike' only). (default:
                              None)
        --bikeUphill BIKEUPHILL
                              Penalty applied to uphill bike travel. (default: None)
        --bikeDownhill BIKEDOWNHILL
                              Penalty applied to downhill bike travel. (default:
                              None)
        --walkSpeed WALKSPEED
                              Walk speed km/h (travelType 'walk' only). (default:
                              None)
        --walkUphill WALKUPHILL
                              Penalty applied to uphill walk travel. (default: None)
        --walkDownhill WALKDOWNHILL
                              Penalty applied to downhill bike travel. (default:
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


### FYI
not all capabilities are available for all plan levels. Refer to the different [plans](https://developers.route360.net/pricing/) to see the specifics.

### Example

    python -m r360_py.cli --travelType walk \
                   --travelTimes 1800 \
                   --source="52.52;13.405" \
                   --outputDir=data/ \
                   --outputFilename=test.geojson \
                   --serviceKey='Your key here' \
                   --serviceUrl=http://service.route360.net/germany/ \
                   --srid=4326 \


## Library Usage

Example how to use the library from Python code:

    #!/usr/bin/env python3
    from r360_py.rest.ServiceExecutor import ServiceExecutor
    from r360_py.util.TravelOptions import TravelOptions
    from r360_py.util.enum.TravelType import TravelType

    travelOptions = TravelOptions()
    travelOptions.setServiceKey('INSERT_YOUR_API_KEY_HERE')
    travelOptions.setTravelType(TravelType.TRANSIT)
    travelOptions.setServiceUrl('https://service.route360.net/westcentraleurope/')
    travelOptions.setTravelTime(10 * 3600)
    travelOptions.setFrameDuration(3 * 3600)
    travelOptions.addSource({"id": "source-1", "lng": 53.5532, "lat": 10.00644})
    travelOptions.addTarget({"id": "target-1", "lng": 53.63265, "lat": 10.00667})

    response = ServiceExecutor().execute_service(travelOptions, "route")
    print(response)


## Testing

Using unit test and nose, API assumes Python 3.x
- rename _tests/config.py.txt_ to _tests/config.py_, add appropriate API key
- run `nosetests -v`
