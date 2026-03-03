from datetime import date, datetime
from enum import StrEnum

from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, SQLModel


class DepartmentEnum(StrEnum):
    ESTOQUISTA = "ESTOQUISTA"


class EmployeeModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(min_length=1, max_length=255, nullable=False)
    birth_date: date = Field(nullable=False)
    department: DepartmentEnum
    email: str = Field(max_length=255, unique=True, nullable=False)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), server_default=func.now()))
    updated_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True), onupdate=func.now()))

    __tablename__ = "employees"
