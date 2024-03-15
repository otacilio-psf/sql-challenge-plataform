from sqlmodel import create_engine, SQLModel, Session, text
from dotenv import load_dotenv
import os
import sys
sys.path.insert(0, './src') 
from core.models import Users, PreAuthCompanyEmail, ChallengeSubmission

load_dotenv()

db_user_password = os.getenv('POSTGRES_ADM_USER_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')

def create_database():
    conn_string = f"cockroachdb://{db_user_password}@{db_host}:26257/defaultdb"
    engine = create_engine(conn_string)
    with Session(engine) as session:
        session.exec(text("CREATE DATABASE backend_db"))
        session.commit()

def main():
    conn_string = f"cockroachdb://{db_user_password}@{db_host}:26257/backend_db"
    engine = create_engine(conn_string)
    SQLModel.metadata.create_all(engine)

if __name__ == '__main__':
    create_database()
    main()