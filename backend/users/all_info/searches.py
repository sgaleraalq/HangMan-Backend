
from users.schemas.user import user_schema
from client.connect_client import client
from users.user import User

def search_user(field:str, key:str):
    try: 
        user = user_schema(client.users.find_one({field: key}))
        return User(**user)
    except:
        return {"error": "No se ha encontrado el usuario"}
