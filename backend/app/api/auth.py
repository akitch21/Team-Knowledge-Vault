from fastapi import APIRouter

router = APIRouter(prefix="/auth",tags=["auth"])

@router.get("/me")
async def read_user():
    return {
  "id": "uuid",
  "username": "taro",
  "email": "taro@example.com",
  "role": "user"
}