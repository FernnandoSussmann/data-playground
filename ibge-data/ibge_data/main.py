import logging
from utils.data_downloader import request_builder


def download(endpoint, api, parameters):
    response = request_builder()(endpoint=endpoint)(api=api)(parameters=parameters)()
    return response.json()



if __name__ == "__main__":
    endpoint = "servicodados.ibge.gov.br"
    api = "api/v1/portal/indicadores"
    parameters = {"periodo": -12}
    data = download(endpoint=endpoint, api=api, parameters=parameters)
    logging.getLogger().setLevel(logging.INFO)
    logging.info(data)
