from bson import ObjectId
from fastapi import APIRouter, HTTPException, status
from users.auth.password import hashing_password
from client.connect_client import client
from users.user import User, UserDB



signup = APIRouter(prefix="/signup")


@signup.post("/", response_model=dict, status_code=201)
async def sign_up(user: User):
    users_client = client["hangman"]["users"]

    # Check if the user is already in the database
    if user.user_name in users_client.find():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User already in the database"
            )
    
    new_user = {"_id":str(ObjectId()),user.user_name:dict(user)}
    users_client.insert_one(new_user)

    return new_user
