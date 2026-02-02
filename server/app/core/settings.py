from pydantic_settings import BaseSettings

class Settings(BaseSettings):
   db_url: str
   debug: bool

   class Config:
      env_file = '.env'
      env_file_encoding = "utf-8"
      extra = "ignore"


settings = Settings()
