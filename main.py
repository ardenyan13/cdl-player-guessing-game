from fastapi import FastAPI

app = FastAPI()

@app.get("/start")
def start_game():
    return {"message": "Call of Duty League Player Guessing Game"}