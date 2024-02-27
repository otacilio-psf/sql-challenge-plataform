from sqlmodel import create_engine, Session, text, SQLModel, Field
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

class ChallengeDB():
    invalid_query_exception = pd.errors.DatabaseError

    def __init__(self):
        db_user = os.getenv('POSTGRES_CHALLENGER_USER')
        db_password = os.getenv('POSTGRES_CHALLENGER_PASSWORD')
        db_host = os.getenv('POSTGRES_HOST')
        conn_string = f"cockroachdb://{db_user}:{db_password}@{db_host}:26257/challenge_db"
        self._engine = create_engine(conn_string)

    def retrive_results(self, query):
        conn = self._engine.connect()
        df = pd.read_sql_query(text(query), conn)
        conn.close()
        return df

    def compare_solution(self, challenge_query, challenge_number):
        conn = self._engine.connect()
        query = f"{challenge_query} EXCEPT SELECT * FROM solution_{challenge_number}"
        df = pd.read_sql_query(text(query), conn)
        conn.close()
        if len(df) == 0:
            return True
        else:
            return False


class BackendDB():

    def __init__(self):
        pass
