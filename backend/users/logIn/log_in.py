from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status


from users.user import User
from users.all_info.searches import search_user
from users.auth.password import verify_password
from users.auth.jwt_authentication import ACCESS_TOKEN_DURATION, SECRET_KEY, ALGORITHM



router = APIRouter(prefix="/auth",
                   tags=["login"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):

    user = search_user("user_name", form.username)

    if type(user) != User: 
        return HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = "User not found in database"
            )
    
    if not verify_password(form.password, user.password):
        return HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Password not correct"
        )

    access_token = {"sub": user.user_name, "exp": datetime.utcnow() + timedelta(weeks=ACCESS_TOKEN_DURATION)}

    return {"access_token": jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM), "token_type": "bearer"}