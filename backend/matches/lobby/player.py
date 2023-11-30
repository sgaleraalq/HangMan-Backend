from pydantic import BaseModel

class Player(BaseModel):
    id: str
    user_name: str
    level: int | None = None
