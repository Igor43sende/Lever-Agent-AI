from fastapi import FastAPI
from app.api.webhook import router as webhook_router

from app.database.connection import engine
from app.database.models import Base

app = FastAPI(title="Lever Agent IA")

app.include_router(webhook_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "Lever-Agent-IA running"}