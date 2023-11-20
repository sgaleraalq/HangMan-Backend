from fastapi import APIRouter, HTTPException, status
from users.user import User
from client.connect_client import users_db_client
from users.auth.password import hashing_password

signup = APIRouter(prefix="/signup")





@signup.post("/", response_model=User, status_code=201)
async def sign_up(user: User):
    if user.user_name in users_db_client["hangman"]["users"].find():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User already exists")
    
    # users_db_client["hangman"]["users"].find()
    
    
    return user
