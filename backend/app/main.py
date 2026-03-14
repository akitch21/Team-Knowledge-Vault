from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.articles import router as articles_router
from app.api.tags import router as tags_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(articles_router)
app.include_router(tags_router)

@app.get("/health",tags=["health"])
def health_check():
    return {"status":"ok"}