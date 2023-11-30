import copy
from fastapi import APIRouter
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

async def check_available_games(lobby: Lobby, player: Player):
    result = await db.find_one({"time":lobby.time})
    
    if result:
        result["players"].append(player.user_name)
        new_players = copy.copy(result["players"])
        result = await db.find_one_and_update({"time":lobby.time}, {"$set":{"players": new_players}})
        final_lobby = await db.find_one({"_id":result["_id"]})
        return Lobby(**lobby_schema(final_lobby))
    else:
        return False

async def create_lobby(lobby: Lobby, player: Player):
    insert_lobby = {"players": [player.user_name], "word": lobby.word, "time": lobby.time}
    result = await db.insert_one(insert_lobby)
    return result


@router.post("/search_game")
async def search_game(data: dict):
    player = Player(**data["player"])
    lobby = Lobby(**data["lobby"])

    active_lobbies = await check_available_games(lobby, player)

    if active_lobbies != False:
        return active_lobbies
    
    else:
        created_lobby = await create_lobby(lobby, player)

        match_maker, match = False, None

        while match_maker == False:
            match = await db.find_one({"_id":created_lobby.inserted_id})
            if type(match) == dict and len(match["players"]) == 2: match_maker = True

        return Lobby(**lobby_schema(match))
