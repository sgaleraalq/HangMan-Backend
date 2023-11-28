from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from users.user import User
from users.all_info.searches import search_user

ALGORITHM = "HS256"
SECRET_KEY = "añabP)YOHI^$UT^)J=)(/(&TGJKBN:NKLY/&RfyPOPKHgoih"
ACCESS_TOKEN_DURATION = 1

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "User not authorized to perform this action", headers={"WWW-Authenticate": "Bearer"})
    try:
        user_name = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
        print(user_name)
        if user_name is None:
            raise exception
    except JWTError:
        raise exception

    return search_user("user_name", user_name)


async def current_user(user: User = Depends(auth_user)):
    print(user)
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    
    return user