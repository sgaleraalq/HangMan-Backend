from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/auth",
                   tags=["login"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    print(form)