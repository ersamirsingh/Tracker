from fastapi import FastAPI
from sqlalchemy.orm import Session
from .db.postgres import engine, Base, SessionLocal

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
   return {"Server is running"}


def get_db():
   db: Session = SessionLocal()
   try:
      yield db
   finally:
      db.close()
