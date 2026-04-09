from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os

from Config.database import connect_db, close_db
from Middlewares.middleware import error_handling_middleware, logging_middleware
from Routes.user_route import user_router

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await close_db()

app = FastAPI(
    title="NoSQL Backend API",
    description="Learning project for backend development with MongoDB",
    version="1.0.0",
    lifespan=lifespan
)

app.middleware("http")(logging_middleware)
app.middleware("http")(error_handling_middleware)

app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "Server running..."}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)