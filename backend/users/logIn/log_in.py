from client.connect_client import client
from fastapi import APIRouter, HTTPException, Depends, status
from users.auth.password import hashing_password
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from users.user import User

login = APIRouter(prefix="/login")

# Make Log In
@login.post("/")
async def log_in(form: OAuth2PasswordRequestForm = Depends()):
    # user_info = client.users.find_one({"user_name":form.username})
    user_info = ["alñskfdsañjañdslfj"]
    return user_info

#     if not user_info:
#         raise HTTPException(status_code=400, detail="Incorrect username")
    
#     user = UserAuth(**user_info)
#     hashed_password = hashing_password(form.password)

#     if hashed_password != hashing_password(user.hashed_password):
#         raise HTTPException(status_code=400, detail="Incorrect password")

#     return user_info