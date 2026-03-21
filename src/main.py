import os
from fastapi import FastAPI
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

if not url or not key:
    print("Error: No se encontraron las variables de entorno de Supabase")
else:
    supabase: Client = create_client(url, key)

@app.get("/")
def read_root():
    return {"message": "API de IA en Render conectada a Supabase"}
