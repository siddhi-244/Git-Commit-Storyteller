# 🎭 Git Commit Storyteller
> Paste your git log → get back a dramatic, cinematic story of your project's journey

---

## 📁 Project Structure
```
git-storyteller/
├── main.py                  # App entry point, mounts routers
├── routers/
│   ├── __init__.py
│   └── story.py             # POST /story, GET /story/styles
├── models/
│   ├── __init__.py
│   ├── request.py           # Pydantic request models
│   └── response.py          # Pydantic response models
├── services/
│   ├── __init__.py
│   └── ai_service.py        # Groq API call + prompt logic
├── core/
│   ├── __init__.py
│   └── config.py            # Settings via pydantic-settings
├── .env                     # GROQ_API_KEY
└── requirements.txt
```

---

## 🔌 Endpoints
| Method | Path | Description |
|--------|------|-------------|
| POST | `/story/generate` | Takes git log + style → returns AI story |
| GET | `/story/styles` | Returns available narrative styles |
| GET | `/health` | Health check |

---

## 🎨 Narrative Styles
- `dramatic` — epic, cinematic, like a movie trailer
- `comedy` — funny, self-deprecating dev humor
- `romance` — the forbidden love between developer and codebase
- `horror` — the bugs, the deadlines, the terror

---

## 🛠️ Tech Stack
- **FastAPI** — API framework
- **Groq** — Free LLM API (Llama 3)
- **Pydantic** — Data validation & settings
- **Uvicorn** — ASGI server

---

## 🪜 Build Steps
1. ✅ `requirements.txt` + `.env` setup
2. ✅ `core/config.py` — environment config
3. ✅ `models/schemas.py` — request/response shapes
4. ✅ `services/ai_service.py` — Groq prompt logic
5. ✅ `routers/story.py` — API routes
6. ✅ `main.py` — wire everything together