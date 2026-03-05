from fastapi import FastAPI
from core.config import settings
from routers.story import router as story_router

app = FastAPI(
    title=settings.app_name,
    description="""
## 🎭 Turn your Git commits into epic stories!

Paste your `git log` output and watch as AI transforms your commit history into a dramatic narrative.

### Features:
- **Multiple Styles**: Choose from funny, serious, sarcastic, brutal, or dramatic tones
- **Customizable Length**: Control the story length with word limits
- **AI-Powered**: Uses Groq's LLaMA model for fast, creative storytelling

### Quick Start:
1. Run `git log --oneline -n 20` in your repo
2. Paste the output into the `/story/generate` endpoint
3. Pick a style and enjoy your project's story!
    """,
    version="1.0.0",
    contact={
        "name": "Git Commit Storyteller",
        "url": "https://github.com/siddhi-244/Git-Commit-Storyteller",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(story_router)


@app.get("/health", tags=["Health"], summary="Health Check", description="Check if the API is running and healthy.")
def health():
    return {"status": "ok", "app": settings.app_name}