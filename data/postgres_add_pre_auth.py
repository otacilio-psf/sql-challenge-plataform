from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os
import sys
sys.path.insert(0, './src') 
from core.models import PreAuthCompanyEmail

load_dotenv()


db_user_password = os.getenv('POSTGRES_ADM_USER_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
database = os.getenv('DATABASE')
conn_string = f"postgresql+psycopg2://{db_user_password}@{db_host}/{database}"

engine = create_engine(conn_string)

def add_domain(domain):
    with Session(engine) as session:
        new_user = PreAuthCompanyEmail(domain=domain)
        session.add(new_user)
        session.commit()

if __name__ == "__main__":
    domain = sys.argv[1]
    add_domain(domain)