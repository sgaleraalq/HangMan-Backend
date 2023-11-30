from pydantic import BaseModel

class Player(BaseModel):
    user_name: str
    level: int | None = None
