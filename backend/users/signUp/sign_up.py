from bson import ObjectId
from fastapi import APIRouter, HTTPException, status
from users.auth.password import hashing_password
from client.connect_client import client
from users.user import User, UserDB



signup = APIRouter(prefix="/signup")

@signup.get("/",status_code=200)
async def loop_users(user: User):
    users_client = client["hangman"]["users"]
    user_exists = any(user.user_name in existing_user.values() for existing_user in users_client.find())
    
    print(user_exists)
    return 



@signup.post("/", response_model=User, status_code=201)
async def sign_up(user: User):
    users_client = client["hangman"]["users"]

    # Check if the user is already in the database
    if user.user_name in users_client.find():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User already in the database"
            )
    
    documento_sin_id = {
    "nombre": "Ejemplo",
    "edad": 25,
    "email": "ejemplo@example.com"
    }

    print(user)
    users_client.insert_one(documento_sin_id)
    return user
