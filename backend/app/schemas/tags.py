from pydantic import BaseModel

# ベーススキーマ
class TagBase(BaseModel):
    id: int
    name: str