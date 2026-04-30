import os
import logging

def download_dataset():
    # IMPORTANTE: El import de Kaggle debe ir AQUÍ ADENTRO
    from kaggle.api.kaggle_api_extended import KaggleApi
    
    try:
        # Forzamos la asignación de nuevo por seguridad
        os.environ['KAGGLE_USERNAME'] = os.getenv("KAGGLE_USERNAME", "")
        os.environ['KAGGLE_KEY'] = os.getenv("KAGGLE_KEY", "")

        api = KaggleApi()
        api.authenticate()
        
        from src.config import KAGGLE_DATASET, RAW_DATA_DIR
        
        if not os.path.exists(RAW_DATA_DIR):
            os.makedirs(RAW_DATA_DIR, exist_ok=True)
            
        logging.info(f"Iniciando descarga de {KAGGLE_DATASET}...")
        api.dataset_download_files(KAGGLE_DATASET, path=RAW_DATA_DIR, unzip=True)
        logging.info("¡Éxito! Dataset descargado en data/raw/")
        
    except Exception as e:
        logging.error(f"Error de autenticación: {e}")
        logging.error("Asegúrate de que KAGGLE_USERNAME y KAGGLE_KEY estén correctos en el .env")
        raise