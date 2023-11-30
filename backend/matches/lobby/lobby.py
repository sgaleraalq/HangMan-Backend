import random
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

from words import list_of_words

lobby = FastAPI()

class Lobby(BaseModel):
    id: Optional[str] = None
    players: list
    word: str = random.choice(list_of_words)
    time: int = 30
