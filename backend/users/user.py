from typing import Dict
from pydantic import BaseModel

model_db = {
    "sgalera":{
        "id"                :   1,
        "user_name"         :   "sgalera",
        "hashed_password"   :   "whatever",
        "name"              :   "Sergio",
        "surname"           :   "Galera",
        "email"             :   "sergiogalera1997@gmail.com"
    },
    "xgalera":{
        "id"                :   2,
        "user_name"         :   "xgalera",
        "hashed_password"   :   "wherever",
        "name"              :   "Xabier",
        "surname"           :   "Galera",
        "email"             :   "xabigalera@gmail.com"
    }
}

class User(BaseModel):
    user_name: str
    email: str | None

class UserDB(BaseModel):
    user_info: Dict[str, User]

class UserAuth(User):
    hashed_password: str

def search_user(database, username:str):
    if username in database:
        return UserAuth(**database[username])