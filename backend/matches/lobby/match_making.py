from typing import Dict
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

async def check_available_games(lobby: Lobby) -> bool:
    result = await db.find_one({"time":lobby.time})
    
    if result:
        result = await db.find_one_and_update({"time":lobby.time}, {"$set":{"rival":True}})
        return True
    else:
        return False

async def create_lobby(lobby: Lobby, player: Player):
    insert_lobby = {
        "players": [player.user_name],
        "word": lobby.word,
        "time": lobby.time,
        "rival": lobby.rival
    }
    result = await db.insert_one(insert_lobby)
    return result

async def wait_for_other_player():
    while True:
        return


@router.post("/search_game")
async def search_game(data: dict):
    player = Player(**data["player"])
    lobby = Lobby(**data["lobby"])

    if await check_available_games(lobby):
        return {"message":"Match Found!"}
    
    else:
        created_lobby = await create_lobby(lobby, player)

        match_maker = False

        while match_maker == False:
            match = await db.find_one({"_id":created_lobby.inserted_id})
            if type(match) == dict: match_maker = match["rival"]

        return {"Message":"Match Found!"}

        # return await lobby