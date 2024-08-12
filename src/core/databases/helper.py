from typing import Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from core.settings import settings


class DatabaseHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False,
        echo_pool: bool = False,
        pool_size: int = 5,
        max_overflow: int = 10,
    ) -> None:
        self.engine: Engine = create_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self.session_factory: sessionmaker = sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
        )

    def dispose(self) -> None:
        self.engine.dispose()

    def session_getter(self) -> Generator[Session, None, None]:
        session: Session = self.session_factory()
        try:
            yield session
        finally:
            session.close()


db_helper: DatabaseHelper = DatabaseHelper(
    url=settings.db.postgres.url,
    echo=settings.db.sqlalchemy.echo,
    echo_pool=settings.db.sqlalchemy.echo_pool,
    pool_size=settings.db.sqlalchemy.pool_size,
    max_overflow=settings.db.sqlalchemy.max_overflow,
)
