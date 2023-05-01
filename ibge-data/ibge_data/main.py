import logging
import pandas as pd
from utils.data_downloader import request_builder
from utils.estrutura_tabela import estrutura


def download(endpoint, api, parameters):
    response = request_builder()(endpoint=endpoint)(api=api)(parameters=parameters)()
    return response.json()


def persistir(subdataset, indicador, metrica):
    df = pd.DataFrame(subdataset.items(), columns=["periodo", metrica])
    logging.debug(df)
    df.to_csv(f"dados/{indicador}.csv", index=False)


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
                    subdataset=dataset[tabela][subtabela]["resultados"],
                    indicador=subestrutura["indicador"],
                    metrica=subestrutura["metrica"],
                )
        else:
            persistir(
                subdataset=dataset[tabela]["resultados"],
                indicador=estrutura["indicador"],
                metrica=estrutura["metrica"],
            )
