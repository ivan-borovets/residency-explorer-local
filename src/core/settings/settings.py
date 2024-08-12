from __future__ import annotations

from pathlib import Path

import rtoml
from pydantic import BaseModel, ConfigDict, Field, PostgresDsn


class SettingsModel(BaseModel):
    model_config = ConfigDict(frozen=True)


class DbPostgres(SettingsModel):
    username: str = Field(alias="POSTGRES_USER")
    password: str = Field(alias="POSTGRES_PASSWORD")
    host: str = Field(alias="POSTGRES_HOST")
    port: int = Field(alias="POSTGRES_PORT")
    path: str = Field(alias="POSTGRES_DB")

    @property
    def url(self) -> str:
        return str(
            PostgresDsn.build(
                scheme="postgresql+psycopg2",
                username=self.username,
                password=self.password,
                host=self.host,
                port=self.port,
                path=self.path,
            )
        )


class DbSqlAlchemy(SettingsModel):
    echo: bool = Field(alias="SQLA_ECHO")
    echo_pool: bool = Field(alias="SQLA_ECHO_POOL")
    pool_size: int = Field(alias="SQLA_POOL_SIZE")
    max_overflow: int = Field(alias="SQLA_MAX_OVERFLOW")

    naming_conventions: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Db(SettingsModel):
    postgres: DbPostgres
    sqlalchemy: DbSqlAlchemy


class Settings(SettingsModel):
    db: Db

    @staticmethod
    def _toml_to_dict(path: Path) -> dict:
        with open(path, mode="r", encoding="utf-8") as f:
            toml_dict: dict = rtoml.load(f)
        return toml_dict

    @classmethod
    def from_file(cls, path: Path, is_docker: bool = False) -> Settings:
        if not path.is_file():
            raise FileNotFoundError(
                f"The file does not exist at the specified path: {path}"
            )
        toml_dict: dict = cls._toml_to_dict(path=path)
        if not is_docker:
            toml_dict["db"]["postgres"]["POSTGRES_HOST"] = "localhost"
        settings_instance: Settings = cls.model_validate(toml_dict)
        return settings_instance


def create_settings() -> Settings:
    base_dir: Path = Path(__file__).parent.parent.parent.parent
    toml_path: Path = base_dir / "config.toml"

    settings_created: Settings = Settings.from_file(path=toml_path)
    return settings_created


settings: Settings = create_settings()
