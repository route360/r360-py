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
        response = requests.get(travel_options.getServiceUrl() + 'v1/' + service, params=params, **request_args)
        self.execution_time = time.time() - start_time
        return self.handle_response(service, response)


    def execute_service_post(self, travel_options, service, data=None, json=None, **request_args):

        params = {
            "key": travel_options.getServiceKey()
        }

        start_time = time.time()
        response = requests.post(travel_options.getServiceUrl() + 'v1/' + service, data=data, json=json, params=params, **request_args)
        self.execution_time = time.time() - start_time
        return self.handle_response(service, response)


    def handle_response(self, service, response):
        if response.status_code == 403:
            raise PermissionError(response.text)
        elif response.status_code != 200:
            logging.getLogger("Service").error("status code: " + str(response.status_code) + ", message: " + response.text)
        else:
            if service == "route":
                json_body = response.text.replace("null(", "").rstrip(")")
                return json.loads(json_body)
            else:
                if (response.text != None and len(response.text) > 0):
                    return json.loads(response.text)
