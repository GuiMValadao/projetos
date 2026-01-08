<<<<<<< HEAD
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = Field(
        default="postgresql+asyncpg://postgres:nd4/3/97@localhost/postgres"
    )


settings = Settings()
=======
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = Field(
        default="postgresql+asyncpg://postgres:nd4/3/97@localhost/postgres"
    )


settings = Settings()
>>>>>>> 9e50be3a49701ce9c08b289a60135d291fc6a2fe
