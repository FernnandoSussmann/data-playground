import os
import requests


def request_builder():
    def define_endpoint(endpoint):
        endpoint = endpoint

        def define_api(api):
            api = api

            def define_parameters(parameters):
                parameters = parameters

                def make_request():
                    return requests.get(
                        os.path.join(f"https://{endpoint}", api), params=parameters
                    )

                return make_request

            return define_parameters

        return define_api

    return define_endpoint
