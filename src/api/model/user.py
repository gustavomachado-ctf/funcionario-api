from datetime import datetime
from enum import StrEnum

from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, SQLModel


class RoleEnum(StrEnum):
    ADMIN = "ADMIN"


class UserModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(max_length=32, unique=True, nullable=False)
    email: str = Field(max_length=255, unique=True, nullable=False)
    password_hash: str = Field(max_length=255, nullable=False)
    role: RoleEnum
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    updated_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True), onupdate=func.now()))

    __tablename__ = "users"
