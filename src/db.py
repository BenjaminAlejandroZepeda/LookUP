import os
from supabase import create_client, Client
from dotenv import load_dotenv


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