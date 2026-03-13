from fastapi import APIRouter
from schemas.tags import TagBase as tag_schemas

router = APIRouter(prefix="/tags",tags=["tags"])

tags = [
    {"id": 1, "name": "Python"},
    {"id": 2, "name": "FastAPI"}
    ]

@router.get("/",response_model=list[tag_schemas])
async def get_tags():
    return [tag_schemas(**tag) for tag in tags]