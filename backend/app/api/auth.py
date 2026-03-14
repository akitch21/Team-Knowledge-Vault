from fastapi import APIRouter

from app.schemas.users import ResponseUser as user_response_schemas
from app.schemas.users import CreateUserRequest as create_user_request_schemas

router = APIRouter(prefix="/auth",tags=["auth"])

users = [
    {"id": 1, "username": "taro", "email": "sample@sample.com", "password_hash": "hashed_password", "role": "user", "created_at": "2024-06-01T12:00:00Z", "updated_at": None},
    {"id": 2, "username": "hanako", "email": "hanako@example.com", "password_hash": "hashed_password", "role": "user", "created_at": "2024-06-01T12:00:00Z", "updated_at": "2024-06-01T12:00:00Z"}
]
    
@router.post("/signup")
async def signup(user_data: create_user_request_schemas):
    return {"message": "User signed up successfully"}
  
@router.post("/login")
async def login():
    return {"message": "User logged in successfully"}

@router.get("/me",response_model=user_response_schemas)
async def read_user():
    return user_response_schemas(**users[0])