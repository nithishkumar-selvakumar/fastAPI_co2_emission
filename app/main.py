from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import get_db, Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}