# IBGE data
Só explorando os dados do IBGE. Provavelmente extraindo e limpando para ver o que da para fazer com isso.

# Como executar
Você deve instalar o [poetry](https://python-poetry.org/). Dentro da pasta `data-playground/ibge-data` aonde extraiu o projeto execute o seguinte comando para atualizar as dependencias:
```sh
poetry update
```
Depois rode:
```sh
poetry run python ibge_data/main.py
```

## Como testar
Execute:
```sh
poetry run pytest
```