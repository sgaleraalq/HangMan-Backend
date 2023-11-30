import random
from fastapi import FastAPI

from words import list_of_words

lobby = FastAPI()

class Lobby:
    def __init__(self):
        self.players: list = []
        self.id: str = ""
        self.word: str = random.choice(list_of_words)
        self.time: int = 30

    