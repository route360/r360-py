import json
import requests
import logging
from r360_py.util.Configuration import Configuration


class ServiceExecutor:
    'This class should be used to query the service'

    def __init__(self):
        return

    def execute_service(self, travel_options, service):

        params = {
            "key": travel_options.getServiceKey(),
            "cfg": json.dumps(Configuration.build(travel_options))
        }

        r = requests.get(travel_options.getServiceUrl() + 'v1/' + service, params=params)

        if r.status_code == 403:
            raise PermissionError(r.text)
        elif r.status_code != 200:
            logging.getLogger("Service").error(r.text)
        else:
            if service == "route":
                json_body = r.text.replace("null(", "").rstrip(")")
                return json.loads(json_body)
            else:
                return json.loads(r.text)
