# Inventory Manager

## Dependencies

* Python 3.10.4
* FastAPI 0.75
* Postgres 12.9

## How to run it

First create a virtual environment

```shell
python -m venv venv
```

Install deps

```shell
pip install -r requirements.txt
```

Create the database

```shell
python create_database.py
```

Running the server

```shell
uvicorn main:app --reload
```
