
from schemas.user import user_schema
from client.connect_client import client
from users.user import User

def search_user(field:str, key:str) -> User | dict:
    try: 
        return User(**user_schema(client.hangman.users.find_one({field: key})))
    except:
        return {"error": "No se ha encontrado el usuario"}
