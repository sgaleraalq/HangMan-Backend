from passlib.context import CryptContext

ALGORITHM = "HS256"
SECRET_STRING = "thisisasecretstringaakjdajfa·$asdf)=7af8shfa098fp8fp F!f2u90fasdf&"

def hashing_password(password: str):
    return password