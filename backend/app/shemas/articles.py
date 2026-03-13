from datetime import datetime

from pydantic import BaseModel, Field
from enum import Enum

class DraftStatus(str, Enum):
    draft = "draft"
    published = "published"


# ベーススキーマ
class ArticleBase(BaseModel):
    id: int
    author_id: int
    title: str = Field(min_length=1, max_length=100, description="記事のタイトル")
    content: str = Field(..., description="記事の内容")
    status: DraftStatus = Field(..., description="記事の公開状態")
    created_at: str = Field(default=datetime.now(), description="記事の作成日時")
    updated_at: datetime | None = None

# レスポンス用スキーマ
class ResponseArticle(ArticleBase):
    pass

# リクエスト用スキーマ
class CreateArticleRequest(BaseModel):
    author_id: int
    title: str
    content: str
    status: DraftStatus = Field(default=DraftStatus.draft, description="記事の公開状態")
    
# 更新用スキーマ
class UpdateArticleRequest(BaseModel):
    title: str | None = None
    content: str | None = None
    status: DraftStatus | None = None
    
# クエリパラメータ用スキーマ
class ArticleQueryParams(BaseModel):
    keyword: str | None = None
    tag: str | None = None
    status: DraftStatus | None = None
    page : int = Field(default=1, ge=1, description="ページ番号")
    page_size : int = Field(default=10, ge=1, le=100, description="1ページあたりのアイテム数")