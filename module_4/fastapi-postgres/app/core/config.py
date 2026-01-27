from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_host: str
    database_port: int
    database_name: str
    database_user: str
    database_password: str

    @property
    def database_url(self) -> str:
        return (
            f"host={self.database_host} "
            f"port={self.database_port} "
            f"dbname={self.database_name} "
            f"user={self.database_user} "
            f"password={self.database_password}"
        )

    class Config:
        env_file = ".env"


settings = Settings()