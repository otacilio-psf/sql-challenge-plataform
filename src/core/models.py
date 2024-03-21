from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Users(SQLModel, table=True):
    __tablename__ = 'users'
    email: str = Field(primary_key=True)
    hash_password: str

class PreAuthCompanyEmail(SQLModel, table=True):
    __tablename__ = 'pre_auth_company_email'
    domain: str = Field(primary_key=True)

class ChallengeSubmission(SQLModel, table=True):
    __tablename__ = 'challenge_submission'
    id: Optional[int] = Field(default=None, primary_key=True)
    challenge_id: int
    email: str
    query: str
    execution_time_ms: float
    max_memory_usage_mib: float
    submission_datetime: datetime = Field(default_factory=datetime.now, nullable=False)
