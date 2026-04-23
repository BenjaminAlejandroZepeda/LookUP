import os
from dotenv import load_dotenv

load_dotenv()

# Inyectar credenciales al entorno del sistema
os.environ['KAGGLE_USERNAME'] = os.getenv("KAGGLE_USERNAME", "")
os.environ['KAGGLE_KEY'] = os.getenv("KAGGLE_KEY", "")

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
KAGGLE_DATASET = "aakashjoshi123/virtual-reality-experiences"