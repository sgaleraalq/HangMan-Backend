from passlib.context import CryptContext
from users.user import User

ALGORITHM = "HS256"
SECRET_KEY = "añabP)YOHI^$UT^)J=)(/(&TGJKBN:NKLY/&RfyPOPKHgoih"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashing_password(password:str) -> str: return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password:str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(user: User):
    return