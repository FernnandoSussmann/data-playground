import logging
from utils.data_downloader import request_builder
from utils.estrutura_tabela import estrutura


def download(endpoint, api, parameters):
    response = request_builder()(endpoint=endpoint)(api=api)(parameters=parameters)()
    return response.json()


def persistir(subdataset, indicador, metrica):
    # TODO Escrever no disco
    logging.info(f"{indicador}/{metrica}: {subdataset}")


if __name__ == "__main__":
    endpoint = "servicodados.ibge.gov.br"
    api = "api/v1/portal/indicadores"
    parameters = {"periodo": -12}
    dataset = download(endpoint=endpoint, api=api, parameters=parameters)
    logging.getLogger().setLevel(logging.INFO)

    for tabela, estrutura in estrutura.items():
        if "indicador" not in estrutura.keys():
            for subtabela, subestrutura in estrutura.items():
                persistir(
                    subdataset=dataset[tabela][subtabela],
                    indicador=subestrutura["indicador"],
                    metrica=subestrutura["metrica"],
                )
        else:
            persistir(
                subdataset=dataset[tabela],
                indicador=estrutura["indicador"],
                metrica=estrutura["metrica"],
            )
