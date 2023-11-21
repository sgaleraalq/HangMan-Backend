from fastapi import APIRouter
from client.connect_client import client


users_info_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@users_info_router.get("/")
async def get_users():
    users_collection = client["hangman"]["users"]
    
    # Obtén todos los documentos como una lista
    users_list = list(users_collection.find())

    # Convierte ObjectId a str en cada documento
    for user in users_list:
        user["_id"] = str(user["_id"])

    return users_list