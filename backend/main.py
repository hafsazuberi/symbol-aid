from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Symbol Aid backend is running!"}
import json
import os

FAVORITES_FILE = "favorites.json"

# GET all favorites
@app.get("/favorites")
def get_favorites():from fastapi import Request

# POST a new favorite
@app.post("/favorites")
async def add_favorite(request: Request):
    body = await request.json()
    symbol = body.get("symbol")
    
    # Load existing favorites
    if os.path.exists(FAVORITES_FILE):
        with open(FAVORITES_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    # Add new symbol if not already present
    if symbol not in data:
        data.append(symbol)
        with open(FAVORITES_FILE, "w") as f:
            json.dump(data, f)

    return {"message": "Favorite added", "favorites": data}

    if not os.path.exists(FAVORITES_FILE):
        return []
    with open(FAVORITES_FILE, "r") as f:
        data = json.load(f)
    return data

