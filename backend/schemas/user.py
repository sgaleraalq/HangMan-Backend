
def user_schema(user) -> dict:
    return {
        "user_name": user["user_name"],
        "name": user["name"],
        "email": user["email"],
        "password": user["password"]
        }

def users_schema(users) -> list:
    return [user_schema(user) for user in users]

def lobby_schema(lobby) -> dict:
    return {
        "players":[""],
        "id": lobby.inserted_id,
        "word": lobby["word"],
        "time": lobby["time"]
    }