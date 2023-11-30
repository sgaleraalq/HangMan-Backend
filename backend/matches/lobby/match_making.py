from fastapi import APIRouter, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

from matches.lobby.lobby import Lobby
from matches.lobby.player import Player
from client.connect_client import uri
from schemas.user import lobby_schema

router = APIRouter(
    prefix="/matchmaking",
    tags=["matchmaking"],
    responses={404: {"description": "Not found"}}
)

db = AsyncIOMotorClient(uri).hangman.lobbies

async def check_available_games(lobby: Lobby) -> Lobby:
    result = lobby_schema(db.find_one({"time":lobby.time}))
    return Lobby(**result)

def create_lobby(lobby: Lobby, player: Player):
    insert_lobby = {
        "players": [player.user_name],
        "word": lobby.word,
        "time": lobby.time
    }
    return db.insert_one(insert_lobby)

@router.post("/search_game")
async def search_game(player: Player, lobby: Lobby):
    if await check_available_games(lobby):
        return {"message":"Match Found!"}
    else:
        return create_lobby(lobby, player)