from fastapi import FastAPI
from core.config import settings
from routers.story import router as story_router

app = FastAPI(
    title=settings.app_name,
    description="Paste your git log, get back a dramatic story of your project's journey.",
    version="1.0.0",
)

app.include_router(story_router)


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok", "app": settings.app_name}