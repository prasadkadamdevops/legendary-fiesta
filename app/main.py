from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="python-devops-demo")

Instrumentator().instrument(app).expose(app)

@app.get("/")
def home():
    return {"message": "Hello from Python DevOps Demo"}

@app.get("/health")
def health():
    return {"status": "ok"}
