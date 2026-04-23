import pandas as pd
import logging

def clean_vr_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Capa Silver: Elimina duplicados, trata nulos y filtra outliers.
    """
    logging.info(f"Registros iniciales: {len(df)}")

    # 1. Eliminar duplicados por User ID
    df = df.drop_duplicates(subset=['UserID'])
    logging.info("Deduplicación completada.")

    # 2. Tratamiento de Nulos: Imputación por Mediana en columnas críticas
    # Esto evita que filas vacías rompan futuros modelos de IA
    cols_to_fix = ['Age', 'Duration', 'ImmersionLevel']
    for col in cols_to_fix:
        if col in df.columns:
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
    
    # 3. Filtro de Outliers (Edad biológicamente posible)
    df = df[(df['Age'] >= 5) & (df['Age'] <= 100)]
    
    logging.info(f"Limpieza finalizada. Registros restantes: {len(df)}")
    return df