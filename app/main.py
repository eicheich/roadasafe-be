from fastapi import FastAPI, HTTPException
from app.config.database import supabase

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Connected to FastAPI"}

@app.get("/users")
def get_items():

    response = supabase.table("users").select("*").execute()
    return response.data

@app.post("/users")
def create_item(name: str, age: int):
    payload = {"name": name, "age": age}
    response = supabase.table("users").insert(payload).execute()
    if not response.data:
        raise HTTPException(status_code=400, detail="Gagal menambahkan data")
    return response.data