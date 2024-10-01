from fastapi import FastAPI, HTTPException

app = FastAPI()

players = ["Shotzzy", "Pred", "Kenny", "Dashy"]

@app.get("/start")
def start_game():
    return {"message": "Call of Duty League Player Guessing Game"}

@app.get("/guess/{player_name}")
def guess_player(player_name: str):
    if player_name in players:
        return {"message": f"Correct {player_name} is the player"}
    
    raise HTTPException(status_code=404)