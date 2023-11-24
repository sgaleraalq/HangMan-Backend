from users.schemas.user import user_schema
from fastapi import APIRouter, HTTPException, status
from users.auth.password import hashing_password
from client.connect_client import client
from users.all_info.searches import search_user_by_email, search_user_by_username
from users.user import User

signup = APIRouter(prefix="/signup")


@signup.post("/", response_model=dict, status_code=201)
async def sign_up(user: User):
    users_client = client["hangman"]["users"]
    
    # Check if user is already in the database
    if type(search_user_by_username(user.user_name)) == User:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail="User already in the database"
        )
    if type(search_user_by_email(user.email)) == User:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail="User already in the database"
        )

    user_dict = dict(user)

    id = users_client.insert_one(user_dict).inserted_id
    new_user = user_schema(users_client.find_one({"_id":id}))

    return User(**new_user)