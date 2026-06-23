from fastapi import FastAPI
from .core.database import  Base, engine
from app.routes.emission_route import router as emission_router

from app.middleware.request_logger import log_request


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.middleware("http")(log_request)

app.include_router(emission_router)

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}
