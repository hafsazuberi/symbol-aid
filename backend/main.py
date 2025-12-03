from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Symbol Aid backend is running!"}
