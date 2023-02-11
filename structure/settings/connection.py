from __future__ import annotations
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from . import URL_TO_DB


class DatabaseConnectionHandler:
    def __init__(self) -> None:
        self.__engine: Engine = create_engine(URL_TO_DB)
        self.session = None

    @property
    def engine(self) -> Engine:
        return self.__engine

    def __enter__(self) -> DatabaseConnectionHandler:
        session = sessionmaker(bind=self.__engine)
        self.session = session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.session.close()
