import os
from supabase import create_client, Client
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Rutas Específicas
RAW_DATA_PATH = os.path.join(DATA_DIR, "raw", "datos_sucios.csv")
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, "processed", "datos_limpios.csv")

# Umbrales Biológicos (Parámetros de Ingeniería)
MAX_VALID_AGE = 110
MIN_VALID_AGE = 0



if os.getenv("ENV") != "production":
    load_dotenv()

_supabase: Client | None = None


def get_supabase() -> Client:
    global _supabase

    if _supabase is None:
        url: str = os.getenv("SUPABASE_URL")
        key: str = os.getenv("SUPABASE_KEY")

        if not url or not key:
            raise Exception("Faltan variables de entorno de Supabase")

        _supabase = create_client(url, key)

    return _supabase