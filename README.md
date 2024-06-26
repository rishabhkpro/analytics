# Analytics

Sample service on how analytics works.

### Setting up virtual environment

It is always better to use virtual environment when working with Python tech stack.

0. Execute below command to install virtualenv dependency package

   `pip3 install virtualenv`

1. Execute below command to create virtual environment. .venv is name, you can give any name

   `python -m venv .venv`

2. Execute below command activate virtual environment.

   `source .venv/bin/activate`

### Installing dependencies

Execute `pip3 install -r requirements.txt` to install all dependenceis for this project

### How to start the server

- Execute below command to start fastapi server

  `uvicorn app:app --reload`

- Execute below command to see API contract in openAPI format.

  `http://localhost:8000/docs#/`

### Event logs and Data

- Event logs are stored in `./logs` folder. This folder can be configurable. You can update this path in `logging_config.py` file

- Events data will be stored `events` table in the database. This can be used for analystics and dashboard data display.
