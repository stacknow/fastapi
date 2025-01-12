from fastapi import FastAPI
from app.routers import example

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Sample"}

# Include additional routers
app.include_router(example.router, prefix="/api", tags=["example"])
