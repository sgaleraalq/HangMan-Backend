from users.user import search_user
from users.auth.password import verify_password



def authenticate_user(database, username: str, password: str):
    user = search_user(database, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user