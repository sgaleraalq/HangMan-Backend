
def user_schema(user) -> dict:
    return {
        "user_name": user["user_name"],
        "name": user["name"],
        "email": user["email"]
        }