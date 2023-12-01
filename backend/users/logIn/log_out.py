from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from users.user import User
from client.connect_client import client
from users.auth.jwt_authentication import current_user

router = APIRouter(
    prefix="/delete",
    tags=["delete"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def delete_user(user: User = Depends(current_user)):
    # User has to be authenticated to delete his account
    result = await client.hangman.users.find_one_and_delete({"user_name": user.user_name})

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {user.user_name} not found"
        )
    else:
        return {
            "message": f"User {user.user_name} deleted successfully"
        }