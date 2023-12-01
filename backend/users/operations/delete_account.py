from fastapi import APIRouter, HTTPException, status, Depends

from users.user import User
from client.connect_client import client
from users.auth.jwt_authentication import current_user

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}}
)

@router.post("/delete_account", response_model=dict, status_code=status.HTTP_201_CREATED)
async def auth_user(user: User = Depends(current_user)):
    # User has to be authenticated to auth his account

    if type(user) == User:
        client.hangman.users.delete_one({"user_name": user.user_name})
        return {"detail": "Account deleted successfully"}

    else:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "User not found in database"
        )
