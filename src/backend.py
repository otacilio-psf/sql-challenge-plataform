from sqlmodel import create_engine, Session, text, select
from dotenv import load_dotenv
import pandas as pd
import os
from models import Users, PreAuthEmails, ChallengeSubmission

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
        db_user = os.getenv('POSTGRES_BACKEND_USER')
        db_password = os.getenv('POSTGRES_BACKEND_PASSWORD')
        db_host = os.getenv('POSTGRES_HOST')
        conn_string = f"cockroachdb://{db_user}:{db_password}@{db_host}:26257/backend_db"
        self._engine = create_engine(conn_string)

    def validate_preauth_email(self, email):
        with Session(self._engine) as session:
            statement = select(PreAuthEmails).where(PreAuthEmails.email == email)
            pre_auth_email = session.exec(statement).first()
            if pre_auth_email:
                return True
            else:
                return False

    def validate_email(self, email):
        with Session(self._engine) as session:
            statement = select(Users).where(Users.email == email)
            email = session.exec(statement).first()
            if email:
                return True
            else:
                return False

    def read_password(self, email):
        with Session(self._engine) as session:
            statement = select(Users).where(Users.email == email)
            user = session.exec(statement).first()
            return user.hash_password
    
    def upsert_user(self, email, hash_password):
        with Session(self._engine) as session:
            statement = select(Users).where(Users.email == email)
            user = session.exec(statement).first()
            if user:
                user.hash_password = hash_password
                session.add(user)
            else:
                new_user = Users(email=email, hash_password=hash_password)
                session.add(new_user)
            session.commit()
    
    def challenge_submission(self, challenge_id, email, query, execution_time_ms):
        with Session(self._engine) as session:
            submission = ChallengeSubmission(challenge_id=challenge_id, email=email, query=query, execution_time_ms=execution_time_ms)
            session.add(submission)
            session.commit()

