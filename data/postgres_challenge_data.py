from sqlmodel import create_engine, Session, text
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

db_user_password = os.getenv('POSTGRES_ADM_USER_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
database = os.getenv('DATABASE')
conn_string = f"postgresql+psycopg2://{db_user_password}@{db_host}/{database}"
engine = create_engine(conn_string)

def create_schema():
    with engine.connect() as connection:
        connection.execution_options(isolation_level="AUTOCOMMIT")
        connection.execute(text("CREATE SCHEMA challenge"))

def load_challenge_data():
    files = os.listdir("data/challenge_datasets")
    for f in files:
        print("Loading dataset:", f)
        table_name = f.split(".")[0]
        pd.read_parquet(f"data/challenge_datasets/{f}").to_sql(table_name, engine, index=False, schema="challenge")

def load_solution():
    files = os.listdir("data/solution_datasets")
    for f in files:
        print("Loading dataset:", f)
        table_name = f.split(".")[0]
        pd.read_csv(f"data/solution_datasets/{f}").to_sql(table_name, engine, index=False, schema="challenge")


if __name__ == '__main__':
    create_schema()
    load_challenge_data()
    load_solution()