import json
import requests
import logging
import time
from r360_py.util.Configuration import Configuration


class ServiceExecutor:
    'This class should be used to query the service'

    def __init__(self):
        self.execution_time = 0
        return

    def get_execution_time(self):
        return self.execution_time

    def execute_service(self, travel_options, service, **request_args):

        params = {
            "key": travel_options.getServiceKey(),
            "cfg": json.dumps(Configuration.build(travel_options))
        }

        start_time = time.time()
        r = requests.get(travel_options.getServiceUrl() + 'v1/' + service, params=params, **request_args)
        self.execution_time = time.time() - start_time

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
