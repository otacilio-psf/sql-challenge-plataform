from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os
import sys
sys.path.insert(0, './src') 
from models import PreAuthEmails

load_dotenv()

db_user = os.getenv('POSTGRES_ADM_USER')
db_password = os.getenv('POSTGRES_ADM_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
conn_string = f"cockroachdb://{db_user}:{db_password}@{db_host}:26257/backend_db"

engine = create_engine(conn_string)

def add_email(email):
    with Session(engine) as session:
        new_user = PreAuthEmails(email=email)
        session.add(new_user)
        session.commit()

if __name__ == "__main__":
    email_list = ["test@email.com"]
    for email in email_list:
        add_email(email)