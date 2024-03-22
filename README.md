# SQL challenge platform

**Objective**
- Be able to run querys against a Postgres (Cockroach Lab) to test the solution
- Be able to evaluate if the results are correct
- Be able to submit the anwser

## Architecture
- Front-end: Streamlit
- Back-end: Postgres

## URL

You can find the running app at:

[https://sql-challenge-platform.streamlit.app/](https://sql-challenge-platform.streamlit.app/)

## How to run localy (Linux)

### Prepare the env

- Create virtual env and install dependencies

```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

- Start an local cockroach db with Docker

```bash
docker run --name my-postgres -p 5432:5432 -v postgres-data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=mysecretpassword -d postgres:16
```

- Create local credentials file
```bash
echo "POSTGRES_ADM_USER_PASSWORD='postgres:mysecretpassword'" >> .env
echo "POSTGRES_BACKEND_USER_PASSWORD='postgres:mysecretpassword'" >> .env
echo "POSTGRES_CHALLENGER_USER_PASSWORD='postgres:mysecretpassword'" >> .env
echo "POSTGRES_HOST='localhost:5432'" >> .env
```

- Create the necessary tables

```bash
python data/postgres_backend.py
python data/postgres_add_pre_auth.py test
python data/postgres_challenge_data.py
```

- Run Streamlit

```bash
streamlit run src/Home.py
```