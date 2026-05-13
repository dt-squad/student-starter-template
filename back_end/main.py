from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .models import Message

app = FastAPI()


@app.get("/api/hello", response_model=Message)
def hello() -> Message:
    return Message(text="Hello from FastAPI")


@app.get("/data")
def hello():
    return dict(
        name="John Doe",
        age=30,
        email="john.doe@example.com")


static_dir = Path(__file__).parent / "static"
if static_dir.is_dir():
    app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
