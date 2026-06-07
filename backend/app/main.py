from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import auth, chat, mood, admin

app = FastAPI(title="Sakhi Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(mood.router, prefix="/mood", tags=["Mood"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])


@app.get("/")
def root():
    return {
        "status": "Sakhi backend running"
    }