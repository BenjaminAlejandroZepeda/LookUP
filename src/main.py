import logging
import pandas as pd
import os
from src.config import RAW_DATA_DIR
from src.extractors.remote_extractor import download_dataset
from src.processors.cleaner import clean_vr_data
from src.processors.transformer import transform_vr_data

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def run_pipeline():
    # 1. Extracción (Capa Bronze)
    download_dataset()
    
    # Buscamos el archivo descargado (el nombre puede variar según Kaggle)
    csv_path = os.path.join(RAW_DATA_DIR, "data.csv")
    
    if not os.path.exists(csv_path):
        logging.error("No se encontró el CSV en la ruta especificada.")
        return

    # Cargamos a memoria
    df_raw = pd.read_csv(csv_path)
    
    print(f"Columnas detectadas: {df_raw.columns.tolist()}")

    # 2. Limpieza (Capa Silver - Parte A)
    df_cleaned = clean_vr_data(df_raw)

    # 3. Transformación (Capa Silver - Parte B)
    df_final = transform_vr_data(df_cleaned)

    # 4. Guardar resultado (Capa Silver Final)
    output_path = csv_path.replace("raw", "processed").replace(".csv", "_limpio.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_final.to_csv(output_path, index=False)
    
    logging.info(f"Pipeline completado. Archivo final en: {output_path}")

if __name__ == "__main__":
    run_pipeline()
    # En src/main.py, justo después de df_raw = pd.read_csv(csv_path)
