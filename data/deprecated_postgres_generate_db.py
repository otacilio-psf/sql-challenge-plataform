from sqlmodel import create_engine, Session, text, SQLModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv('POSTGRES_ADM_USER')
db_password = os.getenv('POSTGRES_ADM_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
conn_string = f"cockroachdb://{db_user}:{db_password}@{db_host}:26257/challenge_db"

engine = create_engine(conn_string)

class Solution1(SQLModel, table=True):
    __tablename__ = 'solution_1'
    country: str = Field(primary_key=True)
    total: float

def populate_db():
    with open('./data/chinook_postgresql.sql', 'r') as sql_file:
        query = text(sql_file.read())

    with Session(engine) as session:
        session.execute(query)
        session.commit()


def populate_solution():
    SQLModel.metadata.create_all(engine)

    solution_1_data = [
        Solution1(country='Germany', total=156.48),
        Solution1(country='Canada', total=303.96),
        Solution1(country='France', total=195.10),
        Solution1(country='Brazil', total=190.10)
    ]

    with Session(engine) as session:
        for item in solution_1_data:
            session.add(item)
        session.commit()

if __name__ == '__main__':
    populate_db()
    populate_solution()