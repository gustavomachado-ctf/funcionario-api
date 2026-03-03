from types import TracebackType
from typing import Self

from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel


class SQLModelDatabase:
    """
    Serviço que gerencia as conexões com o banco de dados.
    """

    __instance: Self | None = None

    def __init__(self, url: str, pool_size: int = 5, echo: bool = False) -> None:
        self.engine = create_engine(url, pool_size=pool_size, echo=echo)
        SQLModel.metadata.create_all(self.engine)
        self.__class__.__instance = self

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool | None:
        self.engine.dispose()

    @classmethod
    def get_session(cls) -> Session:
        return Session(cls.__instance.engine)
