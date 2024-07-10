from fastapi import FastAPI
from .routers import chatBot,db

app = FastAPI()
app.include_router(chatBot.router)
app.include_router(db.router)

@app.get("/")
def read_root():
    return "AstuteAI Chatbot API is running!"

