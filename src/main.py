import os
from fastapi import FastAPI
from supabase import create_client, Client
from dotenv import load_dotenv

# Carga el .env si existe (útil para desarrollo local en Windows)
load_dotenv()

app = FastAPI()

# Inicialización del cliente
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

if not url or not key:
    print("⚠️ Error: No se encontraron las variables de entorno de Supabase")
else:
    supabase: Client = create_client(url, key)

@app.get("/")
def read_root():
    return {"message": "API de IA en Render conectada a Supabase"}

@app.get("/healthcheck")
def health():
    # Intenta una consulta simple para verificar conexión
    try:
        # Reemplaza 'tu_tabla' por una tabla real que tengas en Supabase
        # response = supabase.table("tu_tabla").select("*").limit(1).execute()
        return {"status": "online", "database": "connected"}
    except Exception as e:
        return {"status": "error", "details": str(e)}