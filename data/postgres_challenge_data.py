from sqlmodel import create_engine
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

db_user_password = os.getenv('POSTGRES_ADM_USER_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
conn_string = f"cockroachdb://{db_user_password}@{db_host}:26257/challenge_db"

engine = create_engine(conn_string)

def load_challenge_data():
    files = os.listdir("data/challange_datasets")
    for f in files:
        table_name = f.split(".")[0]
        pd.read_parquet(f"data/challange_datasets/{f}").to_sql(table_name, engine)


def load_solution():
    pass

if __name__ == '__main__':
    load_challenge_data()
    load_solution()