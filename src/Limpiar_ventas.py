import pandas as pd
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(message)s")

def limpiar_csv(ruta_csv: str = "src/ventas_sucias.csv"):
    logging.info(f"--- Leyendo archivo: {ruta_csv} ---")
    df = pd.read_csv(ruta_csv)

    logging.info(f"Registros originales: {len(df)}")
    logging.info(f"\nVista previa (sucio):\n{df.to_string()}\n")

    # 1. Eliminar duplicados
    df = df.drop_duplicates()

    # 2. Eliminar filas con valores nulos o vacíos en columnas críticas
    df = df.replace(r'^\s*$', pd.NA, regex=True)
    df = df.dropna(subset=["nombre", "edad", "monto"])

    # 3. Normalizar tipos
    df["edad"] = pd.to_numeric(df["edad"], errors="coerce")
    df["monto"] = pd.to_numeric(df["monto"], errors="coerce")
    df = df.dropna(subset=["edad", "monto"])

    # 4. Eliminar edades imposibles (fuera del rango 0-120)
    df = df[df["edad"].between(0, 120)]

    # 5. Normalizar fechas a formato YYYY-MM-DD
    df['fecha_compra'] = pd.to_datetime(
        df['fecha_compra'],
        format='mixed',
        errors='coerce')

    # 6. Normalizar texto: ciudad y metodo_pago en Title Case / minúsculas
    df["ciudad"] = df["ciudad"].str.strip().str.title()
    df["metodo_pago"] = df["metodo_pago"].str.strip().str.lower()

    # Resetear índice
    df = df.reset_index(drop=True)
    df = df.dropna()

    logging.info(f"Registros después de limpieza: {len(df)}")
    logging.info(f"\nVista previa (limpio):\n{df.to_string()}\n")
    logging.info("--- Limpieza finalizada correctamente ---")

    return df



df_limpio = limpiar_csv("src/ventas_sucias.csv")