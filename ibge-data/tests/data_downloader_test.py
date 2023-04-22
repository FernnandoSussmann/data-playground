import os

from unittest import mock
from ibge_data.utils.data_downloader import request_builder


@mock.patch("requests.get")
def test_load_function_endpoit(reqsts):
    endpoint = "servicodados.ibge.gov.br"
    api = "api/v1/portal/indicadores"
    parameters = {"periodo": -12}
    expected = {"status_code": 200, "body": {"key": "val"}}

    reqsts.return_value = expected

    response = request_builder()(endpoint=endpoint)(api=api)(parameters=parameters)()

    reqsts.assert_called_with(
        os.path.join(f"https://{endpoint}", api), params=parameters
    )

    response["status_code"] = 200
    response["body"] == {"key": "val"}
