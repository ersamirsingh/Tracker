from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
   db_url: str = Field(..., env="DATABASE_URL")
   # secret_key: str = Field(..., env="SECRET_KEY")
   # debug: bool = Field(False, env="DEBUG")

   class Config:
      env_file = ".env"
      extra = "ignore"

settings = Settings()
