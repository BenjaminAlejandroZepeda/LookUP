import os
import pandas as pd
import logging
from datetime import datetime
from src.config import get_supabase

logging.basicConfig(level=logging.INFO)

info_ingesta = {
    "fecha_ejecucion": "No se ha ejecutado ninguna ingesta aún",
    "ultimo_registro_guardado": None
}

def ingestar_csv_task(ruta_csv: str = "src/abandono_escolar_dataset.csv"):
    try:
        if not os.path.exists(ruta_csv):
            logging.error(f"--- [ERROR] Archivo no encontrado: {ruta_csv} ---")
            return

        logging.info(f"--- Iniciando lectura: {ruta_csv} ---")
        supabase = get_supabase()
        
        df = pd.read_csv(ruta_csv)
        df = df.dropna().drop_duplicates()
        
        if 'abandono' in df.columns:
            df['abandono'] = df['abandono'].astype(int)
            
        datos = df.to_dict(orient='records')
        
        logging.info(f"Subiendo {len(datos)} registros...")
        supabase.table("abandono_escolar").upsert(datos).execute()
        

        info_ingesta["fecha_ejecucion"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        info_ingesta["ultimo_registro_guardado"] = datos[-1] if datos else None
        
        logging.info("--- [ÉXITO] Ingesta finalizada correctamente ---")
        
    except Exception as e:
        logging.error(f"--- [ERROR] Falló el proceso: {e} ---")


def read_csv(path):
    if not os. path.exist(path):
        logging.error(f"Error: Archivo en {path} no existe")
        raise FileNotFoundError(f"No se encontro el archivo en: {path}")
    
    try:
        df = pd.read_csv(path)
        logging.info(f"Exito archivo encontrado y cargado con {len(df)} registros")
        return df
    except Exception as e:
        logging.error(f"Error al leer el CSV: {e}")
        raise