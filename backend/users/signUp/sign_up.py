from fastapi import APIRouter, HTTPException, status
from users.auth.password import hashing_password
from users.all_info.searches import search_user
from users.schemas.user import user_schema
from client.connect_client import client
from users.user import User

router = APIRouter(prefix="/auth")


@router.post("/signup", response_model=User, status_code=status.HTTP_201_CREATED)
async def sign_up(user: User):

    exception = HTTPException(status_code = status.HTTP_409_CONFLICT)

    if type(search_user("user_name", user.user_name)) == User:
        exception.detail = f"User \'{user.user_name}\' already in database"
        raise exception
    
    elif type(search_user("email", user.email)) == User: 
        exception.detail = f"Email \'{user.email}\' already in database"
        raise exception
        

    user.password = hashing_password(user.password)
    user_dict = dict(user)

    id = client.hangman.users.insert_one(user_dict).inserted_id
    new_user = user_schema(client.hangman.users.find_one({"_id":id}))

    return User(**new_user)