import random
from fastapi import FastAPI
from pydantic import BaseModel

from words import list_of_words

lobby = FastAPI()

class Lobby(BaseModel):
    players: list = []
    word: str = random.choice(list_of_words)
    time: int = 30
    rival: bool = False
    