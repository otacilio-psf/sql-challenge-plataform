from sqlmodel import create_engine, Session, SQLModel, Field

class Users(SQLModel, table=True):
    __tablename__ = 'users'
    email: str = Field(primary_key=True)
    hash_password: str

class PreAuthEmails(SQLModel, table=True):
    __tablename__ = 'pre_auth_emails'
    email: str = Field(primary_key=True)