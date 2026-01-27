from fastapi import FastAPI
from app.core.database import init_db
from app.api.v1 import user

app = FastAPI(
    title="FastAPI PostgreSQL App",
    description="A FastAPI application with PostgreSQL",
    version="1.0.0"
)

init_db()

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI PostgreSQL App"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}