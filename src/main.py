from fastapi import FastAPI, HTTPException, BackgroundTasks
from src.db import get_supabase
from src.csv_to_supabase import ingestar_csv_task, info_ingesta 

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "estado_api": "API corriendo",
        "ultima_ingesta": {
            "fecha": info_ingesta["fecha_ejecucion"],
            "ultimo_dato_json": info_ingesta["ultimo_registro_guardado"]
        }
    }

@app.get("/test-db")
def test_connection():
    try:
        supabase = get_supabase()
        response = supabase.table("abandono_escolar").select("*").limit(1).execute()
        return {"status": "ok", "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ingest-csv")
def trigger_csv_ingestion(background_tasks: BackgroundTasks):
    try:
        background_tasks.add_task(ingestar_csv_task, "src/abandono_escolar_dataset.csv")
        return {
            "status": "procesando",
            "message": "La ingesta ha comenzado. Actualiza la página de inicio en unos segundos para ver el resultado."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al iniciar: {e}")