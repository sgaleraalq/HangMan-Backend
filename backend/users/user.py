from pydantic import BaseModel

class User(BaseModel):
    user_name: str
    name: str
    email: str
    password: str