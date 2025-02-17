from collections.abc import Callable
from typing import Annotated, Any, Literal

from pydantic import (
    AliasChoices,
    AmqpDsn,
    AnyUrl,
    BaseModel,
    BeforeValidator,
    Field,
    HttpUrl,
    ImportString,
    PostgresDsn,
    RedisDsn,
    computed_field,
)
from pydantic_settings import BaseSettings, SettingsConfigDict


class SubModel(BaseModel):
    foo: str = "bar"
    apple: int = 1


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    PROJECT_NAME: str = "My Project"

    API_V1_STR: str = "/api/v1"

    SENTRY_DSN: HttpUrl | None = None
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"
    # SQLALCHEMY_DATABASE_URI: PostgresDsn = "postgresql://user:pass@localhost/db"
    # database_url: PostgresDsn = PostgresDsn(
    #     "postgresql://postgres:postgres@localhost:5432/test_db"
    # )
    # database_url: MySQLDsn = MySQLDsn(
    #     "mysql+pymysql://root:123456@localhost:3306/test_db"
    # )
    database_url: str = "mysql+pymysql://root:barn@localhost:3306/test_db"

    FRONTEND_HOST: str = "http://localhost:5173"

    BACKEND_CORS_ORIGINS: Annotated[list[AnyUrl] | str, BeforeValidator(parse_cors)] = []

    @computed_field
    @property
    def all_cors_origins(self) -> list[str]:
        return [str(origin).rstrip("/") for origin in self.BACKEND_CORS_ORIGINS] + [
            self.FRONTEND_HOST
        ]

    auth_key: str = Field(default="default_auth_key", validation_alias="my_auth_key")
    api_key: str = Field(default="default_api_key", alias="my_api_key")

    redis_dsn: RedisDsn = Field(
        "redis://user:pass@localhost:6379/1",
        validation_alias=AliasChoices("service_redis_dsn", "redis_url"),
    )
    pg_dsn: PostgresDsn = "postgres://user:pass@localhost:5432/foobar"
    amqp_dsn: AmqpDsn = "amqp://user:pass@localhost:5672/"

    special_function: ImportString[Callable[[Any], Any]] = "math.cos"

    # to override domains:
    # export my_prefix_domains='["foo.com", "bar.com"]'
    domains: set[str] = set()

    # to override more_settings:
    # export my_prefix_more_settings='{"foo": "x", "apple": 1}'
    more_settings: SubModel = SubModel()

    model_config = SettingsConfigDict(env_prefix="my_prefix_")


settings = Settings()  # type: ignore


if __name__ == "__main__":
    print(settings.model_dump())  # noqa: T201
    """
    {
        'auth_key': 'default_auth_key',
        'api_key': 'default_api_key',
        'redis_dsn': Url('redis://user:pass@localhost:6379/1'),
        'pg_dsn': MultiHostUrl('postgres://user:pass@localhost:5432/foobar'),
        'amqp_dsn': Url('amqp://user:pass@localhost:5672/'),
        'special_function': math.cos,
        'domains': set(),
        'more_settings': {'foo': 'bar', 'apple': 1},
    }
    """
