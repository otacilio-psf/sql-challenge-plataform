from sqlmodel import create_engine, SQLModel, text
from dotenv import load_dotenv
import os
import sys
sys.path.insert(0, './src') 
from core.models import Users, PreAuthCompanyEmail, ChallengeSubmission

load_dotenv()

db_user_password = os.getenv('POSTGRES_ADM_USER_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
database = os.getenv('DATABASE')
conn_string = f"postgresql+psycopg2://{db_user_password}@{db_host}/{database}"
engine = create_engine(conn_string)

def create_schema():
    with engine.connect() as connection:
        connection.execution_options(isolation_level="AUTOCOMMIT")
        connection.execute(text("CREATE SCHEMA backend"))

def main():
    SQLModel.metadata.create_all(engine)

if __name__ == '__main__':
    create_schema()
    main()