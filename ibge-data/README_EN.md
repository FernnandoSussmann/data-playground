# IBGE data
Just playing around with IBGE data. Probably extracting and cleaning at first to afterwards see what can be done with it.

# How to run
You must have [poetry]() installed. Inside `data-playground/ibge-data` folder run the following to update poetry dependencies:
```sh
poetry update
```
Afterwards run:
```sh
poetry run python ibge_data/main.py
```

## How to test
Run:
```sh
poetry run pytest
```