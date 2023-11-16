from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

login_router = FastAPI()

model_db = {
    "sgalera":{
        "user_name" :   "sgalera",
        "password"  :   "whatever",
        "name"      :   "Sergio",
        "surname"   :   "Galera",
        "email"     :   "sergiogalera1997@gmail.com"
    },
    "xgalera":{
        "user_name" :   "xgalera",
        "password"  :   "whatever2",
        "name"      :   "Xabier",
        "surname"   :   "Galera",
        "email"     :   "xabigalera@gmail.com"
    }
}

class User(BaseModel):
    id: int
    user_name: str
    password: str
    name: str
    surname: str
    email: str

@login_router.get("/users_db")
async def get_users():
    return model_db

@login_router.post("/login")
async def log_in(form: OAuth2PasswordRequestForm = Depends()):
    user_info = model_db.get(form.username)
    
    return user_info