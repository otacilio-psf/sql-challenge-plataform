from sqlmodel import create_engine, Session, text, select
from dotenv import load_dotenv
import pandas as pd
import os
from .models import Users, PreAuthCompanyEmail, ChallengeSubmission
load_dotenv()

class ChallengeDB():
    invalid_query_exception = pd.errors.DatabaseError

    def __init__(self):
        db_user_password = os.getenv('POSTGRES_CHALLENGER_USER_PASSWORD')
        db_host = os.getenv('POSTGRES_HOST')
        database = os.getenv('DATABASE')
        conn_string = f"postgresql+psycopg2://{db_user_password}@{db_host}/{database}"
        self._engine = create_engine(conn_string)

    def retrive_results(self, query):
        with self._engine.connect() as connection:
            result_proxy = connection.execute(text("SET search_path to challenge; "+query))
            results = result_proxy.fetchall()
        df = pd.DataFrame(results, columns=result_proxy.keys())
        return df

    def compare_solution(self, challenge_query, challenge_dataset):
        query = f"SET search_path to challenge; {challenge_query} EXCEPT SELECT * FROM expected_{challenge_dataset}"
        df = pd.read_sql_query(text(query), self._engine)
        if len(df) == 0:
            return True
        else:
            return False


class BackendDB():

    def __init__(self):
        db_user_password = os.getenv('POSTGRES_BACKEND_USER_PASSWORD')
        db_host = os.getenv('POSTGRES_HOST')
        database = os.getenv('DATABASE')
        conn_string = f"postgresql+psycopg2://{db_user_password}@{db_host}/{database}"
        self._engine = create_engine(conn_string)

    def validate_preauth_email(self, email):
        with Session(self._engine) as session:
            domain = email.split("@")[-1]
            statement = select(PreAuthCompanyEmail).where(PreAuthCompanyEmail.domain == domain)
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
    
    def challenge_submission(self, challenge_id, email, query, execution_time_ms, total_cost):
        with Session(self._engine) as session:
            submission = ChallengeSubmission(challenge_id=challenge_id, email=email, query=query, execution_time_ms=execution_time_ms, total_cost=total_cost)
            session.add(submission)
            session.commit()

    def get_submission(self, challenge_id):
        with Session(self._engine) as session:
            statement = select(ChallengeSubmission).where(ChallengeSubmission.challenge_id == challenge_id)
            submissions = session.exec(statement).all()
            records = [sub.model_dump() for sub in submissions]
            return pd.DataFrame.from_records(records)


