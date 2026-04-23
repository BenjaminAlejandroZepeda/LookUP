import pandas as pd
import logging

def transform_vr_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Capa Silver: Transformaciones para preparación de IA.
    """
    logging.info("Iniciando transformaciones técnicas...")

    # Transformación 1: Estandarización de categorías (Case Normalization)
    categorical_cols = ['Gender', 'VRHeadset']
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].str.lower().str.strip()

    # Transformación 2: Normalización (Min-Max Scaling) en MotionSickness
    # Esto escala los valores al rango [0, 1]
    if 'MotionSickness' in df.columns:
        min_v = df['MotionSickness'].min()
        max_v = df['MotionSickness'].max()
        if max_v > min_v:
            df['motion_sickness_norm'] = (df['MotionSickness'] - min_v) / (max_v - min_v)

    # Transformación 3: Ingeniería de Atributos (Duración en horas)
    if 'Duration' in df.columns:
        df['duration_hours'] = df['Duration'] / 60

    logging.info("Transformaciones aplicadas con éxito.")
    return df