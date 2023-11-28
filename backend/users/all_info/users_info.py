from fastapi import APIRouter, Depends

from users.user import User
from client.connect_client import client
from users.schemas.user import users_schema
from users.auth.jwt_authentication import current_user


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[User])
async def get_users():    
    return users_schema(client.users.find())

@router.get("/me")
async def me(user: User = Depends(current_user)):
    return user