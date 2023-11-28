from users.schemas.user import users_schema
from users.user import User
from fastapi import APIRouter
from client.connect_client import client

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[User])
async def get_users():    
    return users_schema(client.users.find())