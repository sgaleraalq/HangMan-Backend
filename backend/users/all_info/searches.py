
from users.schemas.user import user_schema
from client.connect_client import client
from users.user import User

def search_user_by_email(email:str):
    try: 
        user = user_schema(client.hangman.users.find_one({"email": email}))
        return User(**user)
    except:
        return {"error": "No se ha encontrado el usuario"}
    
def search_user_by_username(username:str):
    try: 
        user = user_schema(client.hangman.users.find_one({"user_name": username}))
        return User(**user)
    except:
        return {"error": "No se ha encontrado el usuario"}