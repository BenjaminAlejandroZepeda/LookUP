from fastapi import FastAPI, HTTPException
from src.db import get_supabase

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "API corriendo 🚀"}


@app.get("/test-db")
def test_connection():
    try:
        supabase = get_supabase()

        response = supabase.table("items").select("*").limit(1).execute()

        return {
            "status": "ok",
            "data": response.data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))