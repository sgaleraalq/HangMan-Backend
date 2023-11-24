from fastapi import APIRouter, HTTPException, status
from users.auth.password import hashing_password
from users.all_info.searches import search_user
from users.schemas.user import user_schema
from client.connect_client import client
from users.user import User

signup = APIRouter(prefix="/signup")


@signup.post("/", response_model=User, status_code=201)
async def sign_up(user: User):    
    # Check if user is already in the database
    if type(search_user("email", user.email)) == User or type(search_user("user_name", user.user_name)) == User:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail="User already in the database"
        )

    user_dict = dict(user)

    id = client.users.insert_one(user_dict).inserted_id
    new_user = user_schema(client.users.find_one({"_id":id}))

    return User(**new_user)