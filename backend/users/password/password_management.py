from passlib.context import CryptContext

ALGORITHM = "HS256"
SECRET_STRING = "thisisasecretstringaakjdajfa·$asdf)=7af8shfa098fp8fp F!f2u90fasdf&"


pwd_context  = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashing_password(plain_password: str):
    return pwd_context.hash(plain_password)

def verify_password(plain_password: str, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)
