from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from api.repository.database import SQLModelDatabase


def get_database_session_service() -> Generator[Session]:
    with SQLModelDatabase.get_session() as session:
        yield session


DatabaseDependency = Annotated[Session, Depends(get_database_session_service)]
