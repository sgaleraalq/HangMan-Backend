from fastapi import APIRouter, HTTPException, Depends, status
from ..password.password_management import hashing_password
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from ..user import User, UserAuth, model_db

login = APIRouter(prefix="/login")

# Make Log In
@login.post("/")
async def log_in(form: OAuth2PasswordRequestForm = Depends()):
    user_info = model_db.get(form.username)

    if not user_info:
        raise HTTPException(status_code=400, detail="Incorrect username")
    
    user = UserAuth(**user_info)
    hashed_password = hashing_password(form.password)

    if hashed_password != hashing_password(user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    return user_info