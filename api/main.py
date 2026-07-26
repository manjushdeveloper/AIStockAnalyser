from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="AI Stock Analyzer",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "AI Stock Analyzer API is Running"
    }