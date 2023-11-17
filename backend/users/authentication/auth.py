from ..user import search_user
from ..password.password_management import verify_password


def authenticate_user(fake_db, username: str, password: str):
    user = search_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user