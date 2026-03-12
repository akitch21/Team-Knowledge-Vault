from fastapi import APIRouter
from typing import Any

router = APIRouter(prefix="/articles",tags=["articles"])

articles = [
    {"id": 1, "title": "FastAPIメモ", "content": "FastAPIの基本"},
    {"id": 2, "title": "Next.jsメモ", "content": "Next.jsの基本"}
]


@router.get("/")
async def get_articles() -> list[dict[str,Any]]:
    return articles