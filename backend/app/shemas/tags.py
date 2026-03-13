from pydantic import BaseModel, Field

# ベーススキーマ
class TagBase(BaseModel):
    id: int
    name: str