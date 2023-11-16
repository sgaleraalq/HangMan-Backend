from fastapi import APIRouter, HTTPException
from ..user import User, model_db
from ..password.password_management import hashing_password

signup = APIRouter(prefix="/signup")


@signup.post("/", response_model=User, status_code=201)
async def sign_up(user: User):
    if user.user_name in model_db:
        raise HTTPException(status_code=422, detail="El usuario ya existe")
    
    # model_db[user.user_name] = user
    return model_db
