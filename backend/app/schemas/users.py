from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    user = "user"

# ベーススキーマ
class UserBase(BaseModel):
    id: int
    username: str = Field(min_length=3, max_length=30, description="ユーザーの名前")
    email: str = Field(..., description="ユーザーのメールアドレス")
    password_hash: str = Field(min_length=8, description="ユーザーのパスワードハッシュ")
    role: UserRole = Field(default=UserRole.user, description="ユーザーの役割")
    created_at: str = Field(default=datetime.now(), description="ユーザーの作成日時")
    updated_at: datetime | None = None
    
    
# レスポンス用スキーマ
class ResponseUser(UserBase):
    pass

# リクエスト用スキーマ
class CreateUserRequest(BaseModel):
    username: str
    email: str
    password_hash: str
    role: UserRole = Field(default=UserRole.user, description="ユーザーの役割")