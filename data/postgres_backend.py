from sqlmodel import create_engine, SQLModel
from dotenv import load_dotenv
import os
import sys
sys.path.insert(0, './src') 
from models import Users, PreAuthEmails

load_dotenv()

db_user = os.getenv('POSTGRES_ADM_USER')
db_password = os.getenv('POSTGRES_ADM_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
conn_string = f"cockroachdb://{db_user}:{db_password}@{db_host}:26257/backend_db"

engine = create_engine(conn_string)

def main():
    SQLModel.metadata.create_all(engine)

if __name__ == '__main__':
    main()