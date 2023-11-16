from fastapi import FastAPI
from users.logIn import log_in
from users.signUp import sign_up
from fastapi.staticfiles import StaticFiles

app = FastAPI()


app.include_router(log_in.router)
app.include_router(sign_up.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return "Hi FastAPI!!"

@app.get("/url")
async def url():
    return { "url_curso" : "https://sgaleraa.com/python" }