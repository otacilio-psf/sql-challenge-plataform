# SQL challenge platform

**Objective**
- Be able to run querys against a Postgres (Cockroach Lab) to test the solution
- Be able to evaluate if the results are correct
- Be able to submit the anwser

## Architecture
- Front-end: Streamlit
- Back-end: Cockroach Lab serveless (free) cluster

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
docker run --rm -d --name=roach -p 8080:8080 -p 26257:26257 -v roach-data:/cockroach/cockroach-data cockroachdb/cockroach:latest start-single-node --insecure
```

- Create local credentials file
```bash
echo "POSTGRES_ADM_USER_PASSWORD='root'" > .env
echo "POSTGRES_BACKEND_USER_PASSWORD='root'" >> .env
echo "POSTGRES_CHALLENGER_USER_PASSWORD='root'" >> .env
echo "POSTGRES_HOST='localhost'" >> .env
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