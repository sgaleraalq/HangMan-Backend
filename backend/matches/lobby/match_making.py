import copy
from fastapi import APIRouter
from motor.motor_asyncio import AsyncIOMotorClient

from matches.lobby.lobby import Lobby
from matches.lobby.player import Player
from client.connect_client import uri
from schemas.schemas import lobby_schema

router = APIRouter(
    prefix="/matchmaking",
    tags=["matchmaking"],
    responses={404: {"description": "Not found"}}
)

db = AsyncIOMotorClient(uri).hangman.lobbies

async def check_available_games(lobby: Lobby, player: Player):
    # Find a lobby that has only 1 player in players list and same time as the one that is being created
    result = await db.find_one({"time":lobby.time, "players": {"$size": 1}})
    
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


## MAYBE CREATE A NEW DATA WHICH TAKES THE ID OF THE LOBBY CREATED?

@router.post("/cancel_game")
async def cancel_game(lobby: Lobby):
    # TODO still missing deleting the lobby game
    result = await db.delete_one({"_id":lobby.id})

    return result