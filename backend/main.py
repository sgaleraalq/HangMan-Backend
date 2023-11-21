from fastapi import FastAPI
from users.logIn import log_in
from users.signUp import sign_up
from users.all_info import users_info

app = FastAPI()

app.include_router(log_in.login)
app.include_router(sign_up.signup)
app.include_router(users_info.users_info_router)


@app.get("/")
async def root():
    return "Hi, this is just a simple backend for user auth"


@app.get("/url")
async def url():
    return {"url_github": "https://github.com/sgaleraalq/HangMan-Backend/"}
