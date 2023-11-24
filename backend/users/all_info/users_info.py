from fastapi import APIRouter
from client.connect_client import client


users_info_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@users_info_router.get("/")
async def get_users():    
    return list(client.find())